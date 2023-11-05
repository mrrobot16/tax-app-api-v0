from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional

from app.models.conversation import ConversationModel
from app.enums.user import UserAuthType, UserRole

class UserModel(BaseModel):
    id: str
    name: Optional[str] = None
    email: EmailStr
    conversations: List[ConversationModel] = []
    active: bool = True
    auth_type: UserAuthType = Field(default = UserAuthType.EMAIL_PASSWORD, alias = 'auth_type')
    role: UserRole = Field(default = UserRole.USER, alias = 'role')
    created_at: datetime
    updated_at: datetime

    class Config:
        use_enum_values = True
        populate_by_name = True
        

class UserPrivateModel(UserModel):
    password: Optional[str] = None
    class Config(UserModel.Config):
        pass
