from pydantic import BaseModel
from datetime import datetime

from app.models.message import MessageGroupModel, MessageModel

class ConversationModel(BaseModel):
    id: str
    user_id: str
    name: str
    messages: list[MessageModel] = []
    message_groups: list[MessageGroupModel] = []
    active: bool = True
    created_at: datetime
    updated_at: datetime

    def add_message(self, message: MessageModel):
        self.messages.append(message)
    
    def add_message_group(self, message_group: MessageGroupModel):
        self.message_groups.append(message_group)