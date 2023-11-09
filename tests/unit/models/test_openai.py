from app.models.openai import OpenAIChatCompletionObjectResponseModel
from tests.fixtures.openai import openai_chat_completion_object_response_data

def test_chat_completion():
    openai = OpenAIChatCompletionObjectResponseModel(**openai_chat_completion_object_response_data)
    assert openai.choices[0]['message']['content'] == openai_chat_completion_object_response_data['choices'][0]['message']['content']