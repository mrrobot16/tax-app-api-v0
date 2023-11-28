from pydantic import BaseModel
from datetime import datetime

from app.models.message import MessageGroupModel, MessageModel
from app.utils import generate_timestamp, generate_unique_id

class ConversationModel(BaseModel):
    id: str = generate_unique_id()
    user_id: str # Only required field.
    name: str = "New Chat"
    messages: list[MessageModel] = []
    message_groups: list[MessageGroupModel] = []
    active: bool = True
    created_at: datetime = generate_timestamp()
    updated_at: datetime = generate_timestamp()

    def add_message(self, message: MessageModel):
        self.messages.append(message)
        self.updated_at = generate_timestamp()
    
    def add_message_group(self, message_group: MessageGroupModel):
        self.message_groups.append(message_group)
        self.updated_at = generate_timestamp()