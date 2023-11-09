from app.enums.user import UserRole
from app.enums.openai import OpenAIModel, OpenAIObjectType
from tests.fixtures.openai import openai_service
from tests.fixtures.message import user_message

def test_chat_completion_gpt3(openai_service):
    response = openai_service.chat_completion(
        engine = OpenAIModel.GPT_3_5_TURBO_16K.value
    )
    assert response is not None

    open_ai_chat_completion_api = response['open_ai_chat_completion_api']

    assert len(open_ai_chat_completion_api['choices']) > 0
    assert open_ai_chat_completion_api['choices'][0] is not None
    assert open_ai_chat_completion_api['choices'][0]['message']['role'] == UserRole.ASSISTANT.value
    assert open_ai_chat_completion_api['choices'][0]['message']['content'] is not None
    assert open_ai_chat_completion_api['object'] == OpenAIObjectType.CHAT_COMPLETION.value
    assert open_ai_chat_completion_api['model'] == OpenAIModel.GPT_3_5_TURBO_16K.value

    api = response['api']
    message = api['message']
    assert api is not None
    assert message is not None
    assert message['role'] == UserRole.ASSISTANT.value
    assert message['content'] is not None
    

def test_chat_completion_gpt4(openai_service):
    response = openai_service.chat_completion(
        engine = OpenAIModel.GPT_4_1106_PRE.value, 
        prompt = user_message['content']
    )

    open_ai_chat_completion_api = response['open_ai_chat_completion_api']

    assert response is not None
    assert len(open_ai_chat_completion_api['choices']) > 0
    assert open_ai_chat_completion_api['choices'][0]['message'] is not None
    assert open_ai_chat_completion_api['choices'][0]['message']['role'] == UserRole.ASSISTANT.value
    assert open_ai_chat_completion_api['choices'][0]['message']['content'] is not None
    assert open_ai_chat_completion_api['object'] == OpenAIObjectType.CHAT_COMPLETION.value
    assert open_ai_chat_completion_api['model'] == OpenAIModel.GPT_4_1106_PRE.value

    api = response['api']
    message = api['message']
    assert api is not None
    assert message is not None
    assert message['role'] == UserRole.ASSISTANT.value
    assert message['content'] is not None


