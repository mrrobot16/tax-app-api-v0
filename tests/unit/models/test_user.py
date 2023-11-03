from app.models.user import UserModel, UserPrivateModel
from tests.fixtures.models.user import user_data, user_private_data

def test_user_instanciated():
    user = UserModel(**user_data)
    user_private = UserPrivateModel(**user_data, password=user_private_data["password"])
    assert user.id == user_private.id
    assert user.name == user_private.name
    assert user.email == user_private.email
    assert user.conversations == user_private.conversations
    assert user.active == user_private.active
    assert user.created_at == user_private.created_at
    assert user.updated_at == user_private.updated_at
    assert user.auth_type == user_private.auth_type
    assert user_private.password == user_private_data["password"]
    assert user.created_at == user_private.created_at
    assert user.updated_at == user_private.updated_at