from pydantic import BaseModel

from enums.openai import OpenAIModel
class OpenAIChatCompletionRequestModel(BaseModel):
    model: OpenAIModel = OpenAIModel.GPT_4 
    content: str
    role: str = "user"

# NOTE: The current response for ChatCompletion is formatted is like this.
class OpenAIChatCompletionObjectResponseModel(BaseModel):
    id: str # str ie: "chatcmpl-89jaHxop3jAcGGTzeSZhpoJzP1g0y"
    object: str # str ie: "chat.completion"
    created: int # int ie: 1697330869
    model: str # str ie: "gpt-4"
    choices: list # array [ { index: int, message: { role: str ie: assistant, content: str }, finish_reason: str } ]
    usage: dict # dict { prompt_tokens: int, completion_tokens: int, total_tokens: int }

class ChatCompletionResponseModel(BaseModel):
    message: dict # dict { role: str ie: assistant, content: str }