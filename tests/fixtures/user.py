import random
import pytest

from app.services.user import UserService
from app.utils import generate_unique_id, generate_timestamp


@pytest.fixture
def user_service():
    service = UserService
    yield service

# user_id = generate_unique_id()
user_id = "cefece6f-3a77-493c-b"

emails = [
    "h@testng.com",
    "i@testng.com",
    "j@testng.com",
    "k@testng.com",
]

names = [
    "John",
    "Jane",
    "Bob",
    "Alice",
    "Mary",
    "Mark",
    "Steve",
]

user_name = random.choice(names)

user_email = random.choice(emails)

user_data = {
    'id': user_id,
    'name': user_name,
    'email': user_email,
    'conversations': [],
    'active': True,
    'created_at': generate_timestamp(),
    'updated_at': generate_timestamp(),
    'auth_type': 'email-password'
}

user_private_data = {
    'password': 'password'
}