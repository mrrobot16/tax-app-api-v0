from pydantic import BaseModel

class MessageModel(BaseModel):
    id: str
    user_id: str
    conversation_id: str
    content: str
    role: str
    created_at: str

class MessageGroupModel(BaseModel):
    id: str
    user_id: str
    conversation_id: str
    messages: list[MessageModel]
    created_at: str