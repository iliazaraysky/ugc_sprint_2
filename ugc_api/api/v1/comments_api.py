from fastapi import APIRouter, Depends
from models.comments import UserComment
from services.comments_service import (UserCommentService,
                                       get_user_comment_service)

router = APIRouter()


@router.post("/")
async def user_comment(data: UserComment,
                       comment_post: UserCommentService = Depends(get_user_comment_service)):
    user_comment = await comment_post.post_comment(data)
    return user_comment
