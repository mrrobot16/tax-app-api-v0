from fastapi import FastAPI

from controllers.openai import openai_controller
from controllers.users import users_controller
from controllers.conversations import conversations_controller

def configure_routes(app: FastAPI):
    app.include_router(openai_controller, prefix="/openai", tags=["OpenAI Controller"])
    app.include_router(users_controller, prefix="/users", tags=["Users Controller"])
    app.include_router(conversations_controller, prefix="/conversations", tags=["Conversations Controller"])