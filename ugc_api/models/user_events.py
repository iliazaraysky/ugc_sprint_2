from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, Field


class BaseData(BaseModel):
    film_id: UUID
    user_id: UUID
    created_at: datetime = Field(default_factory=datetime.now)


class UserFilmView(BaseData):
    view_time: date


class UserFilmFavorites(BaseData):
    favorites: bool


class UserFilmComment(BaseData):
    text: str


class UserFilmLike(BaseData):
    like: bool
