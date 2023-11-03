from enum import Enum
from pydantic import BaseModel, EmailStr

from app.models.conversation import ConversationModel

class UserRole(Enum):
    ADMIN = 'admin'
    USER = 'user'
    SYSTEM = 'system'
    ASSISTANT = 'assistant'

class UserAuthType(Enum): 
    EMAIL_PASSWORD = 'email-password'

class UserModel(BaseModel):
    id: str
    name: str | None = None
    email: EmailStr | None = None
    conversations: list[ConversationModel] = []
    role: UserRole = UserRole.USER
    active: bool = True
    auth_type: UserAuthType = UserAuthType.EMAIL_PASSWORD
    created_at: str 
    updated_at: str

class UserPrivateModel(UserModel):
    password: str | None = None