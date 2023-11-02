from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
