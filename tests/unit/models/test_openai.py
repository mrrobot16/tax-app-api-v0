from app.models.openai import OpenAIChatCompletionResponseModel
from tests.fixtures.openai import openai_response_data

def test_chat_completion():
    openai = OpenAIChatCompletionResponseModel(**openai_response_data)
    assert openai.choices[0]['message']['content'] == openai_response_data['choices'][0]['message']['content']