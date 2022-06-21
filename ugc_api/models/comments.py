from pydantic import BaseModel
from typing import Optional


class UserComment(BaseModel):
    user_id: Optional[str]
    film: Optional[str]
    comment: Optional[str]
