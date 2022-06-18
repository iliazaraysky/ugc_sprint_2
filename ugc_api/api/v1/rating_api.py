from fastapi import APIRouter, Depends
from models.rating import UserFilmRating
from services.rating_service import (RatingEventService,
                                     get_rating_event_service)

router = APIRouter()


@router.post('/rating_event')
async def user_film_rating(
        data: UserFilmRating,
        rating_event: RatingEventService = Depends(get_rating_event_service)):
    post_event = await rating_event.post_event(data)
    return post_event
