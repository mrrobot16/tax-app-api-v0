from fastapi.testclient import TestClient
from app.utils import generate_unique_id

from tests.fixtures.conversation import conversation_data, conversation_id
from tests.fixtures.message import user_message
from tests.fixtures.user import user_id

from app.main import app

client = TestClient(app)

def test_conversations_status():
    response = client.get("/conversations/status")
    assert response.status_code == 200

def test_get_all():
    response = client.get("/conversations/")
    assert response.status_code == 200

def test_get_all_by_user():
    response = client.get(f"/conversations/user/{user_id}")
    assert response.status_code == 200

def test_get():
    response = client.get(f"/conversations/{conversation_id}")
    assert response.status_code == 200

def _test_new():
    response = client.post(f"/conversations/new", json = conversation_data)
    assert response.status_code == 200

def test_new_conversation_chat_completion_message():
    json = {
        "conversation": {
            "user_id": user_id,
        },
        "message": {
            "user_id": user_id,
            **user_message
        },
    }
    response = client.post("/conversations/new/message/chat-completion", json = json)
    assert response.status_code == 200

def test_new_message():
    json = {
        "user_id": user_id,
        "conversation_id": conversation_id,
        **user_message,
    }
    response = client.post(f"/conversations/message/new", json = json)
    assert response.status_code == 200

def test_new_chat_completion_message():
    json = {
        "user_id": user_id,
        "conversation_id": conversation_id,
        **user_message,
    }
    response = client.post(f"/conversations/message/chat-completion", json = json)
    assert response.status_code == 200

def test_update():
    json = {
        "name": f"New Conversation Name {generate_unique_id()}",
    }
    response = client.put(f"/conversations/{conversation_id}", json = json)
    assert response.status_code == 200


def test_deactivate():
    response = client.put(f"/conversations/deactivate/{conversation_id}")
    assert response.status_code == 200

def test_activate():
    response = client.put(f"/conversations/activate/{conversation_id}")
    assert response.status_code == 200
