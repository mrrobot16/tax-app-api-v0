import random

from models.conversation import Conversation
from db.firebase import firestore_db
from tests.fixtures.models.conversation import conversation_fixture

conversation = Conversation(firestore_db)

messages = conversation_fixture['messages']

random_message = messages[random.randint(0, len(messages) - 1)]
random_new_message = messages[random.randint(0, len(messages) - 1)]

id = "7ba4cca9-4115-4a5d-a"
user_id = "cefece6f-3a77-493c-b"

def test_get_all():
    conversations = conversation.get_all()
    assert len(conversations) > 0

def test_get_all_by_user():
    get_conversation = conversation.get_all_by_user(user_id)
    assert len(get_conversation) > 0

def test_get():
    get_conversation = conversation.get(id)
    assert get_conversation['id'] == id

def test_new():
    new_conversation = conversation.new(user_id)
    assert new_conversation['user_id'] == user_id


def test_new_message():
    message = random_new_message
    new_message = conversation.new_message(user_id, id, message)
    get_conversation = conversation.get(id)
    assert new_message['user_id'] == user_id
    assert new_message['conversation_id'] == id
    assert new_message['content'] == message['content']
    assert new_message['role'] == message['role']

def test_update():
    conversation.update(id, "New Conversation name")
    assert conversation.get(id)['name'] == "New Conversation name"

def test_deactivate():
    conversation.deactivate(id)
    assert conversation.get(id)['active'] == False

