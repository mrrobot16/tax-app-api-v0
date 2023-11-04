from pydantic import BaseModel, EmailStr
from datetime import datetime

from app.models.conversation import ConversationModel
from app.enums.user  import UserRole, UserAuthType

class UserModel(BaseModel):
    id: str
    name: str | None = None
    email: EmailStr | None = None
    conversations: list[ConversationModel] = []
    role: UserRole = UserRole.USER
    active: bool = True
    auth_type: UserAuthType = UserAuthType.EMAIL_PASSWORD
    created_at: datetime
    updated_at: datetime

class UserPrivateModel(UserModel):
    password: str | None = None