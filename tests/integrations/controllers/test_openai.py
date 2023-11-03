import time
import random

from controllers.openai import openai_controller

def test_health(client):
    response = client.get("/openai/health")
    

def test_chat_completion(client):
    json = {
        "prompt": "Tell me about the IRS"
    }
    response = client.post("/openai/chat-completion", json = json)
    assert response.status_code == 200