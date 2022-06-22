from pydantic import BaseModel
from typing import Optional


class BaseData(BaseModel):
    user_id: Optional[str]
    film: Optional[str]


class UserComment(BaseData):
    comment: Optional[str]


class UserFilmLike(BaseData):
    like: bool
