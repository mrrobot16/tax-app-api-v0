from app.utils import generate_unique_id, generate_timestamp

id = generate_unique_id()

user_data = {
    'id': generate_unique_id(),
    'name': 'John Doe',
    'email': 'johndoe@gmail.com',
    'conversations': [],
    'active': True,
    'created_at': generate_timestamp(),
    'updated_at': generate_timestamp(),
    'auth_type': 'email-password'
}

user_private_data = {
    'password': 'password'
}

emails = [
    "h@testng.com",
    "i@testng.com",
    "j@testng.com",
    "k@testng.com",
]