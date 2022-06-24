import sentry_sdk
import httpx
import uvicorn as uvicorn
from aiokafka import AIOKafkaProducer
from fastapi import FastAPI, Request, Response
from fastapi.responses import ORJSONResponse
from motor.motor_asyncio import AsyncIOMotorClient

from api.v1 import rating_api, user_event_api
from core import config
from db import kafka, mongodb

sentry_sdk.init(dsn=config.SENTRY_SDK_DSN, traces_sample_rate=1.0)

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.middleware("http")
async def sentry_exception(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        with sentry_sdk.push_scope() as scope:
            scope.set_context("request", request)
            sentry_sdk.capture_exception(e)
        raise e


@app.on_event('startup')
async def startup():
    mongodb.mongo = AsyncIOMotorClient('mongodb://mongo-fastapi:27017')
    kafka.producer = AIOKafkaProducer(bootstrap_servers=[f'{config.KAFKA_HOST}:{config.KAFKA_PORT}'])
    await kafka.producer.start()


@app.on_event('shutdown')
async def shutdown():
    await kafka.producer.stop()
    await mongodb.mongo.stop()


app.include_router(rating_api.router, prefix='/api/v1/events/rating', tags=['rating_event'])
app.include_router(user_event_api.router, prefix='/api/v1/films/user-event', tags=['user_events'])


# Проверяет Auth сервис. Обращается по адресу.
# Если в заголовке есть валидный токен, предоставляет доступ к контенту
@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    headers = request.headers
    resp = await check_user('http://nginx/auth/v1/usercheck', dict(headers))
    print("This is resp", resp)
    if resp.status_code == 200:
        response = await call_next(request)
        return response
    return Response(status_code=401)


async def check_user(url, headers):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=headers)
        return resp


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000
    )
