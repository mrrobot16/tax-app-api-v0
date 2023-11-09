import time

from fastapi import status
from fastapi.testclient import TestClient

from app.main import app
from tests.fixtures.user import user_data, user_private_data

client = TestClient(app)

def test_user_status():
    response = client.get("/users/status")
    assert response.status_code == status.HTTP_200_OK

def test_get_users():
    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK

def test_get_user():
    response = client.get(f"users/{user_data['id']}")
    assert response.status_code == status.HTTP_200_OK

def test_new_user():
    user = {
        'name': user_data['name'],
        'email': user_data['email'],
        'password': user_private_data['password'],
        'auth_type': user_data['auth_type'],
    }
    response = client.post("/users/new", json = user)
    assert response.status_code == status.HTTP_200_OK

def test_update_user():
    response = client.put(f"/users/{user_data['id']}", json = {"email": user_data["email"], "name": user_data['name']})
    assert response.status_code == status.HTTP_200_OK

def test_deactivate_user():
    response = client.put(f"/users/deactivate/{user_data['id']}")
    assert response.status_code == status.HTTP_200_OK

def test_activate_user():
    time.sleep(3)
    response = client.put(f"/users/activate/{user_data['id']}")
    assert response.status_code == status.HTTP_200_OK