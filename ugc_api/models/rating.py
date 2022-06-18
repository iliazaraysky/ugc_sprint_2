from uuid import UUID

from pydantic import BaseModel


class UserFilmRating(BaseModel):
    film_id: UUID
    user_id: UUID
    rating: float
