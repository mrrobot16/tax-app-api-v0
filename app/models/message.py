from pydantic import BaseModel
from datetime import datetime

from app.enums.user import UserRole

class MessageModel(BaseModel):
    id: str
    user_id: str
    conversation_id: str
    content: str
    role: UserRole
    created_at: datetime

class MessageGroupModel(BaseModel):
    id: str
    user_id: str
    conversation_id: str
    messages: list[MessageModel]