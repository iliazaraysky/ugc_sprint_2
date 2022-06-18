import uvicorn as uvicorn
from aiokafka import AIOKafkaProducer
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import rating_api
from core import config
from db import kafka

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    kafka.producer = AIOKafkaProducer(bootstrap_servers=[f'{config.KAFKA_HOST}:{config.KAFKA_PORT}'])
    await kafka.producer.start()


@app.on_event('shutdown')
async def shutdown():
    await kafka.producer.stop()


app.include_router(rating_api.router, prefix='/api/v1/events/rating', tags=['rating_event'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000
    )