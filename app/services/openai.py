import openai

from app.constants.openai import (
    OPENAI_ENGINE, 
    OPENAI_TEMPERATURE, OPENAI_MAX_TOKENS, 
    OPENAI_ASSISTANT_PROMPT, OPENAI_SYSTEM_PROMPT, OPENAI_USER_PROMPT, 
    OPENAI_API_KEY_DEV
)
from app.models.openai import OpenAIChatCompletionResponseModel

class OpenAIService:

    def __init__(self, keys = OPENAI_API_KEY_DEV):
        openai.api_key = keys

    def chat_completion(
            self,
            prompt = OPENAI_USER_PROMPT['content'], 
            engine = OPENAI_ENGINE,
            system_prompt = OPENAI_SYSTEM_PROMPT, 
            assistant_prompt = OPENAI_ASSISTANT_PROMPT,
            temperature = OPENAI_TEMPERATURE,  
            max_tokens = OPENAI_MAX_TOKENS,
    ):
        try:
            # NOTE: prompt.encode().decode() is used to remove non-ASCII characters from the prompt.
            user_prompt = {
                "role": "user",
                "content": prompt.encode(encoding = 'ASCII', errors = 'ignore').decode() + ". "
            }
            response = openai.ChatCompletion.create(
                model = engine,
                messages = [
                    system_prompt,
                    assistant_prompt,
                    user_prompt,
                ],
                temperature = temperature,
                max_tokens = max_tokens
            )
            openai_response_model = OpenAIChatCompletionResponseModel(**response)
            return openai_response_model
        except Exception as error:
            return f"chat_completion error: {error}"