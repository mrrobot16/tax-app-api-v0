import random

from controllers.conversation import conversation_controller
from tests.fixtures.models.conversation import conversation_fixture

messages = conversation_fixture['messages']
random_message = messages[random.randint(0, len(messages) - 1)]
random_new_message = messages[random.randint(0, len(messages) - 1)]

id = "7ba4cca9-4115-4a5d-a"
user_id = "cefece6f-3a77-493c-b"

def test_health(client):
    response = client.get("/conversations/health")
    assert response.status_code == 200

def test_get_all(client):
    response = client.get("/conversations/")
    assert response.status_code == 200

def test_get_all_by_user(client):
    response = client.get(f"/conversations/user/{user_id}")
    assert response.status_code == 200

def test_get(client):
    response = client.get(f"/conversations/{id}")
    assert response.status_code == 200

def test_new(client):
    json = {
        "user_id": user_id
    }
    response = client.post(f"/conversations/new", json=json)
    assert response.status_code == 200

def test_new_message(client):
    json = {
        "user_id": user_id,
        "message": random_new_message
    }
    response = client.post(f"/conversations/message/new/{id}", json=json)
    assert response.status_code == 200

def test_update(client):
    json = {
        "name": random_new_message,
    }
    response = client.put(f"/conversations/update/{id}", json=json)
    assert response.status_code == 200


def test_deactivate(client):
    response = client.put(f"/conversations/deactivate/{id}")
    assert response.status_code == 200
