from app.enums.user import UserRole
from app.enums.openai import OpenAIModel, OpenAIObjectType
from tests.fixtures.openai import openai_service
from tests.fixtures.message import user_message

def test_chat_completion_gpt3(openai_service):
    response = openai_service.chat_completion(
        engine = OpenAIModel.GPT_3_5_TURBO_16K.value
    )
    assert response is not None
    assert len(response.choices) > 0
    assert response.choices[0].message is not None
    assert response.choices[0].message.role == UserRole.ASSISTANT.value
    assert response.choices[0].message.content is not None
    assert response.object == OpenAIObjectType.CHAT_COMPLETION.value
    assert response.model == OpenAIModel.GPT_3_5_TURBO_16K.value

def test_chat_completion_gpt4(openai_service):
    response = openai_service.chat_completion(
        engine = OpenAIModel.GPT_4.value, 
        prompt = user_message['content']
    )
    assert response is not None
    assert len(response.choices) > 0
    assert response.choices[0].message is not None
    assert response.choices[0].message.role == UserRole.ASSISTANT.value
    assert response.choices[0].message.content is not None
    assert response.object == OpenAIObjectType.CHAT_COMPLETION.value
    assert response.model == OpenAIModel.GPT_4.value
