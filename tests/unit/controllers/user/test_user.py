import time
import random

from controllers.user import user_controller

from tests.fixtures.models.user import emails

random_email = emails[random.randint(0, len(emails) - 1)]

user_id = "cefece6f-3a77-493c-b"

def test_health(client):
    response = client.get("/users/health")
    assert response.status_code == 200

def test_get_all(client):
    response = client.get("/users/")
    assert response.status_code == 200

def test_get(client):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200

def test_new(client):
    json = {
        "name": "test_name",
        "email": "test_controller_new_email@testing.com",
        "password": "test_password"
    }
    response = client.post("/users/new", json=json)
    assert response.status_code == 200

def test_update(client):
    json = {
        "email": random_email,
    }
    response = client.put(f"/users/update/{user_id}", json=json)
    assert response.status_code == 200

def test_deactivate(client):
    response = client.put(f"/users/deactivate/{user_id}")
    assert response.status_code == 200

def test_activate(client):
    time.sleep(3)
    response = client.put(f"/users/activate/{user_id}")
    assert response.status_code == 200