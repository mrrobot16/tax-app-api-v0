import time
import random

from db.firebase import firestore_db, firestore
from services.user import get_users, new_user, get_user, update_user, delete_user, deactivate_user, activate_user
from tests.fixtures.models.user import emails

random_email = emails[random.randint(0, len(emails) - 1)]
id = "cefece6f-3a77-493c-b"

def test_get_users():
    users = get_users()
    assert len(users) > 0

def test_get_user():
    user = get_user(id)
    assert user["id"] == id

def test_new_user():
    email = "testing_new_user_service@testing.com"
    user = new_user("testing_new_user_service@testing.com", None)
    assert user["email"] == "testing_new_user_service@testing.com"

def test_update_user():
    email = random_email
    user = update_user(id, email)
    assert user["email"] == email

def test_deactivate_user():
    user = deactivate_user(id)
    assert user["active"] == False

def test_activate_user():
    time.sleep(3)
    user = activate_user(id)
    assert user["active"] == True

# Not really needing to test this, but it's nice to have.
# def test_delete_user(id):
#     return user.delete(id)