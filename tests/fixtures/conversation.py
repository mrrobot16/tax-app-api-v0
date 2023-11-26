import pytest

from app.services.conversation import ConversationService
from app.utils import generate_unique_id
from tests.fixtures.user import user_data

id = generate_unique_id()
conversation_id = '9ec7c0f5-5bcd-4e7c-a'
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