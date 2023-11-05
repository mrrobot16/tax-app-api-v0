from app.constants.openai import OPENAI_ENGINE, OPENAI_ENGINE_GPT_4
from tests.fixtures.openai import openai_service
from tests.fixtures.message import user_message

def test_chat_completion(openai_service):
    response = openai_service.chat_completion()
    assert response is not None
    assert len(response.choices) > 0
    assert response.choices[0].message is not None
    assert response.choices[0].message.role == 'assistant'
    assert response.choices[0].message.content is not None
    assert response.object == 'chat.completion'
    # NOTE: Model being pass is 'gpt-3.5-turbo-16k' by default
    # But OpenAI chatCompletion api response return gpt-3.5-turbo-16k-0613
    assert response.model == OPENAI_ENGINE

def test_chat_completion_gpt4(openai_service):
    response = openai_service.chat_completion(
        engine = OPENAI_ENGINE_GPT_4, 
        prompt = user_message['content']
    )
    assert response is not None
    assert len(response.choices) > 0
    assert response.choices[0].message is not None
    assert response.choices[0].message.role == 'assistant'
    assert response.choices[0].message.content is not None
    assert response.object == 'chat.completion'
    assert response.model == OPENAI_ENGINE_GPT_4
