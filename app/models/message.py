from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


from app.enums.user import UserRole
from app.utils import generate_timestamp, generate_unique_id

class MessageModel(BaseModel):
    id: str = generate_unique_id()
    user_id: str # required field.
    conversation_id: str | None
    content: str # required field.
    role: UserRole = Field(default = 'user', alias = 'role')
    created_at: datetime = generate_timestamp()
    updated_at: datetime = generate_timestamp()
    class Config:
        use_enum_values = True
        populate_by_name = True

class MessageGroupModel(BaseModel):
    id: str = generate_unique_id()
    user_id: str
    conversation_id: str
    messages: list[MessageModel]
    created_at: datetime = generate_timestamp()
    up_voted: bool | None = None
    down_voted: bool | None = None
    rating: int | None = None
    comment: str | None = None