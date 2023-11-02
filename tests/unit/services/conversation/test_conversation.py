import time
import random

from db.firebase import firestore_db, firestore
from services.conversation import get_conversations, get_conversations_by_user, new_conversation, new_message, update_conversation, deactivate_conversation, get_conversation
from tests.fixtures.models.conversation import conversation_fixture

messages = conversation_fixture["messages"]
random_message = messages[random.randint(0, len(messages) - 1)]
random_new_message =  messages[random.randint(0, len(messages) - 1)]

id = "7ba4cca9-4115-4a5d-a"
user_id = "cefece6f-3a77-493c-b"

def test_get_conversations():
    conversations = get_conversations()
    assert len(conversations) > 0

def test_get_conversations_by_user():
    conversations = get_conversations_by_user(user_id)
    assert len(conversations) > 0

def test_new_conversation():
    conversation = new_conversation(user_id)
    assert conversation["user_id"] == user_id


def test_get_conversation():
    conversation = get_conversation(id)
    assert conversation["id"] == id

def test_new_message():
    message = new_message(user_id, id, random_new_message)
    assert message["user_id"] == user_id
    assert message['conversation_id'] == id
    assert message['content'] == message['content']
    assert message['role'] == message['role']

def test_update_conversation():
    update_conversation(id, "New Conversation name")
    conversation = get_conversation(id)
    assert conversation['name'] == "New Conversation name"

def test_deactivate():
    deactivate_conversation(id)
    conversation = get_conversation(id)
    assert conversation['active'] == False