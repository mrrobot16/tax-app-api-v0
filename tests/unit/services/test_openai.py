from tests.fixtures.openai import openai_service

def test_chat_completion(openai_service):
    response = openai_service.chat_completion()
    assert response is not None