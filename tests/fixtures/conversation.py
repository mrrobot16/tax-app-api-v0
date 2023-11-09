import pytest
import random

from app.enums.user import UserRole
from app.services.conversation import ConversationService
from app.utils import generate_unique_id
from tests.fixtures.user import user_data, user_id

id = generate_unique_id()
conversation_id = '220bb6e8-4489-4ee0-a'
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