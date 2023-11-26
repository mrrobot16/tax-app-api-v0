from typing import Union
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import requests

from models.openai import OpenAIChatCompletionObjectResponseModel, OpenAIChatCompletionRequestModel, ChatCompletionResponseModel
from services.openai import openai_service
from constants.openai import OPENAI_API_KEY_DEV

openai_controller = APIRouter()

@openai_controller.post("/chat-completion")
def chat_gpt4(request: OpenAIChatCompletionRequestModel) -> Union[OpenAIChatCompletionObjectResponseModel, ChatCompletionResponseModel]:
    chat_completion_response = openai_service().chat_completion(prompt = request.content)
    return JSONResponse(content = chat_completion_response['api'])

@openai_controller.get("/status")
def check_openai_status():
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY_DEV}',
    }

    try:
        response = requests.get('https://api.openai.com/v1/engines', headers=headers)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        return response.json()  # Return the JSON from the response
    except requests.exceptions.HTTPError as http_err:
        # You can handle different status codes using response.status_code if needed
        raise HTTPException(status_code=500, detail=f"HTTP error occurred: {http_err}")
    except Exception as err:
        # Generic exception catch. The raise here will stop the execution and return the error
        raise HTTPException(status_code=500, detail=f"An error occurred: {err}")
