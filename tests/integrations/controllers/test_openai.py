import time
import random

from fastapi.testclient import TestClient

from app.main import app
from tests.fixtures.openai import openai_request_data

client = TestClient(app)

def test_health():
    response = client.get("/openai/status")
    assert response.status_code == 200
    

def test_chat_completion():
    response = response = client.post("/openai/chat-completion", json = openai_request_data)
    assert response.status_code == 200