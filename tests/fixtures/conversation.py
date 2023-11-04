from app.utils import generate_unique_id, generate_timestamp
from tests.fixtures.user import user_data

id = generate_unique_id()
conversation_data = {
    'id': id,
    'user_id': user_data['id'],
    'name': f'Test Conversation id: {id}',
    "messages": [],
    "active": True,
}