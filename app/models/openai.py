from pydantic import BaseModel

# NOTE: The current response for ChatCompletion is formatted like this.
class OpenAIChatCompletionResponseModel(BaseModel):
    id: str # str ie: "chatcmpl-89jaHxop3jAcGGTzeSZhpoJzP1g0y"
    object: str # str ie: "chat.completion"
    created: int # int ie: 1697330869
    model: str # str ie: "gpt-4"
    choices: list # array [ { index: int, message: { role: str ie: assistant, content: str }, finish_reason: str } ]
    usage: dict # dict { prompt_tokens: int, completion_tokens: int, total_tokens: int }