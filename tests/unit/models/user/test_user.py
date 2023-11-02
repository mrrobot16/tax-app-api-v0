import time
import random

from models.user import User
from tests.fixtures.models.user import user_fixture
from db.firebase import firestore_db
from tests.fixtures.models.user import emails

user = User(firestore_db)
id = "cefece6f-3a77-493c-b"
random_email = emails[random.randint(0, len(emails) - 1)]

def test_get_all():
    users = user.get_all()
    assert len(users) > 0

def test_new():
    new_user = user.new(user_fixture["email"], user_fixture["password"], user_fixture["conversations"])
    new_user = user.get(new_user["id"])
    assert new_user['email'] == "johndoe@example.com"
    assert new_user['conversations'] == []

def test_get():
    get_user = user.get(id)
    assert get_user['id'] == id

def test_update():
    email = random_email
    user.update(id, email)
    assert user.get(id)['email'] == email

def test_deactivate_user():
    user.deactivate(id)
    assert user.get(id)['active'] == False

def test_activate_user():
    time.sleep(3)
    user.activate(id)
    assert user.get(id)['active'] == True