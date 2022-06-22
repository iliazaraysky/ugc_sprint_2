from functools import lru_cache
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from db.mongodb import get_mongo
from models.user_events import UserComment, UserFilmLike
from fastapi.encoders import jsonable_encoder


class UserEventService:
    def __init__(self, mongo: AsyncIOMotorClient):
        self.mongo = mongo

    async def post_comment(self, comment: UserComment):
        db = self.mongo.comments
        comment = jsonable_encoder(comment)
        await db['comment'].insert_one(comment)
        return {'message create': "ok"}

    async def post_like(self, like: UserFilmLike):
        db = self.mongo.likes
        like = jsonable_encoder(like)
        await db['like'].insert_one(like)
        return {'message create': "ok"}


@lru_cache()
def get_user_event_service(
        mongo: AsyncIOMotorClient = Depends(get_mongo)
) -> UserEventService:
    return UserEventService(mongo)
#
#
# class UserEventLike:
#     def __init__(self, mongo: AsyncIOMotorClient):
#         self.mongo = mongo
#
#     async def post_like(self, like: UserFilmLike):
#         db = self.mongo.likes
#         like = jsonable_encoder(like)
#         await db['like'].insert_one(like)
#         return {'message create': "ok"}
#
#
# @lru_cache()
# def get_user_event_like(
#         mongo: AsyncIOMotorClient = Depends(get_mongo)
# ) -> UserEventLike:
#     return UserEventLike(mongo)
