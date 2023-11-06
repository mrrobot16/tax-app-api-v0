import warnings

from tests.fixtures.user import user_data, user_private_data, user_service
from app.models.user import UserModel
from app.enums.user import UserRole, UserAuthType
from app.utils import hash_password
from app.constants import filter_warning_message

def test_get_all(user_service):
    users = user_service.get_all()
    assert users is not None
    assert len(users) > 0

def test_get(user_service):
    warnings.filterwarnings("ignore", category = UserWarning, message = filter_warning_message)
    user = user_service.get(user_data["id"])
    user_model = UserModel(**user)
    assert user_model is not None
    assert user_model.id == user_data["id"]

def _test_new(user_service):
    user = user_service.new(
        email = user_data["email"], 
        name = user_data["name"], 
        password = user_private_data["password"],
        role = "user",
        auth_type = "email-password"
    )
    assert user is not None
    assert user["id"] is not None
    assert user["name"] == user_data["name"]
    assert user["email"] == user_data["email"]
    assert user["role"] == UserRole.USER.value
    assert user["conversations"] == []
    assert user["auth_type"] == UserAuthType.EMAIL_PASSWORD.value
    assert user["created_at"] is not None
    assert user["updated_at"] is not None

def test_update(user_service):
    update_data = {
        "name": user_data["name"],
        "email": user_data["email"]
    }
    user = user_service.update(
        user_data["id"],
        update_data
    )
    assert user is not None
    assert user["id"] is not None
    assert user["name"] == update_data["name"]
    assert user["email"] == update_data["email"]

def test_deactivate(user_service):
    user = user_service.deactivate(user_data["id"])
    assert user is not None
    assert user["id"] is not None
    assert user["active"] == False

def test_activate(user_service):
    user = user_service.activate(user_data["id"])
    assert user is not None
    assert user["id"] is not None
    assert user["active"] == True