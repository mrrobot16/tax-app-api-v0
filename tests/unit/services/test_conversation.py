import warnings
import time

from app.enums.openai import OpenAIModel, OpenAIObjectType
from app.services.conversation import ConversationService

from tests.fixtures.conversation import conversation_data, conversation_service, conversation_id
from tests.fixtures.message import user_message
from tests.fixtures.user import user_id
from tests.fixtures.tasks import tasks

from app.enums.user import UserRole
from app.models.conversation import ConversationModel
from app.models.message import MessageModel
from app.constants import filter_warning_message

def test_get_all(conversation_service):
    conversations = conversation_service.get_all()

    assert conversations is not None
    assert len(conversations) > 0


def test_get_all_by_user(conversation_service):
    conversations = conversation_service.get_all_by_user(user_id)

    assert conversations is not None
    assert len(conversations) > 0

def test_get(conversation_service):
    warnings.filterwarnings("ignore", category = UserWarning, message = filter_warning_message)
    conversation = conversation_service.get(conversation_id)
    conversation_model = ConversationModel(**conversation)

    assert conversation_model is not None
    assert conversation_model.id == conversation_id

def _test_new(conversation_service):
    conversation_model = ConversationModel(**conversation_data)
    conversation = conversation_service.new(conversation_model)

    assert conversation is not None
    assert conversation["id"] is not None
    assert conversation["user_id"] is not None
    assert conversation["name"] == conversation_data["name"]
    assert conversation["message_groups"] == []
    assert conversation["messages"] == []
    assert conversation["active"] == True
    assert conversation["created_at"] is not None
    assert conversation["updated_at"] is not None

def _test_new_message():
    conversation_service = ConversationService()
    message_data = {
        "user_id": user_id,
        "conversation_id": conversation_id,
        **user_message,
    }
    message_model = MessageModel(**message_data)

    message = conversation_service.new_message(message_model)

    assert message is not None
    assert message["id"] is not None
    assert message["user_id"] == message_data["user_id"]
    assert message["role"] == user_message["role"]
    assert message["created_at"] is not None
    assert message["updated_at"] is not None


def test_update(conversation_service):
    update_data = {
        "name": conversation_data["name"],
    }

    conversation = conversation_service.update(
        conversation_id,
        update_data
    )

    assert conversation is not None
    assert conversation["id"] is not None
    assert conversation["name"] == update_data["name"]

def test_deactivate(conversation_service):
    conversation = conversation_service.deactivate(conversation_id)

    assert conversation is not None
    assert conversation["id"] is not None
    assert conversation["active"] == False

def test_activate(conversation_service):
    time.sleep(2)
    conversation = conversation_service.activate(conversation_id)

    assert conversation is not None
    assert conversation["id"] is not None
    assert conversation["active"] == True

def test_new_chat_completion_message(tasks):
    conversation_service = ConversationService()
    message_data = {
        "user_id": user_id,
        "conversation_id": conversation_id,
        **user_message,
    }
    message_model = MessageModel(**message_data)
    
    response = conversation_service.new_chat_completion_message(message_model, tasks)
    assert response is not None
    
    open_ai_chat_completion_api = response['open_ai_chat_completion_api']
    assert len(open_ai_chat_completion_api['choices']) > 0
    assert open_ai_chat_completion_api['choices'][0]['message'] is not None
    assert open_ai_chat_completion_api['choices'][0]['message']['role'] == UserRole.ASSISTANT.value
    assert open_ai_chat_completion_api['choices'][0]['message']['content'] is not None
    assert open_ai_chat_completion_api['object'] == OpenAIObjectType.CHAT_COMPLETION.value
    assert open_ai_chat_completion_api['model'] == OpenAIModel.GPT_4_1106_PRE.value

    api = response['api']
    message = api['message']
    assert api is not None
    assert message is not None
    assert message['role'] == UserRole.ASSISTANT.value
    assert message['content'] is not None
