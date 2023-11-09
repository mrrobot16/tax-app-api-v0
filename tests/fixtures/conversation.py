import pytest

from app.services.conversation import ConversationService
from app.utils import generate_unique_id
from tests.fixtures.user import user_data

id = generate_unique_id()
conversation_id = '052a7d1e-fcef-457b-9'
conversation_data = {
    'id': id,
    'user_id': user_data['id'],
    'name': f'Test Conversation id: {id}',
    "messages": [],
    "active": True,
}

@pytest.fixture
def conversation_service():
    service = ConversationService
    yield service