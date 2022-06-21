from functools import lru_cache
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from db.mongodb import get_mongo
from models.comments import UserComment
from fastapi.encoders import jsonable_encoder


class UserCommentService:
    def __init__(self, mongo: AsyncIOMotorClient):
        self.mongo = mongo

    async def post_comment(self, comment: UserComment):
        db = self.mongo.comments
        comment = jsonable_encoder(comment)
        await db['comment'].insert_one(comment)
        return {'message create': "ok"}


@lru_cache()
def get_user_comment_service(
        mongo: AsyncIOMotorClient = Depends(get_mongo)
) -> UserCommentService:
    return UserCommentService(mongo)
