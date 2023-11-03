from services.openai import chat_completion

def test_chat_completion():
    response = chat_completion("What is a 1040?")
    assert response is not None