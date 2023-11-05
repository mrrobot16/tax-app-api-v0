import openai

from app.config import env_variables
from app.constants.openai import OPENAI_ENGINE, OPENAI_TEMPERATURE, OPENAI_MAX_TOKENS, OPENAI_ASSISTANT_PROMPT, OPENAI_SYSTEM_PROMPT, OPENAI_USER_PROMPT
from app.utils import generate_timestamp

OPENAI_API_KEY_DEV = env_variables.OPENAI_API_KEY_DEV

class OpenAIService:

    def __init__(self, engine = OPENAI_ENGINE, keys = OPENAI_API_KEY_DEV, temperature = OPENAI_TEMPERATURE,  max_tokens = OPENAI_MAX_TOKENS):
        self.keys = keys
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        openai.api_key = self.keys

    def chat_completion(self, prompt = OPENAI_USER_PROMPT['content'], system_prompt = OPENAI_SYSTEM_PROMPT, assistant_prompt = OPENAI_ASSISTANT_PROMPT):
        self.created_at = generate_timestamp()
        user_prompt = prompt.encode(encoding = 'ASCII', errors = 'ignore').decode() + ". " + OPENAI_USER_PROMPT['content']
        try:
            openai_response = openai.ChatCompletion.create(
                model = self.engine,
                messages = [
                    system_prompt,
                    assistant_prompt,
                    { "role": "user", "content": user_prompt }
                ],
                temperature = self.temperature,
                max_tokens = self.max_tokens
            )
            print('openai_response', openai_response)
            return openai_response
            # openai_response = OpenAIResponse(**openai_response).to_dict()
            # content = openai_response['choices'][0]['message']['content']
            # role = openai_response['choices'][0]['message']['role']
            # response = {
            #     "api": {
            #         "id": self.id,
            #         "created_at": self.created_at,
            #         "prompt": user_prompt,
            #         "content": content,
            #         "role": role,
            #     },
            #     "openai": openai_response 
            # }
            # return response
        except Exception as error:
            return f"chat_completion error: {error}"
        
def get_openai_service():
    return OpenAIService()