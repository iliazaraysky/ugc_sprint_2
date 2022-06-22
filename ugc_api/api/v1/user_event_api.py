from fastapi import APIRouter, Depends
from models.user_events import UserComment, UserFilmLike
from services.user_event_service import (UserEventService,
                                         get_user_event_service)

# from services.user_event_service import (UserEventLike,
#                                          get_user_event_like)

router = APIRouter()


@router.post("/add-comment")
async def user_comment(data: UserComment,
                       comment_post: UserEventService = Depends(get_user_event_service)):
    user_comment = await comment_post.post_comment(data)
    return user_comment


@router.post("/add-like")
async def user_like(data: UserFilmLike,
                    like_post: UserEventService = Depends(get_user_event_service)):

    user_like = await like_post.post_like(data)
    return user_like
