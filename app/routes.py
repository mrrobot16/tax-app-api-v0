from fastapi import FastAPI

from app.controllers.openai import openai_controller
from app.controllers.users import user_controller


def configure_routes(app: FastAPI):
    app.include_router(openai_controller, prefix="/openai", tags=["OpenAI Controller"])
    app.include_router(user_controller, prefix="/users", tags=["User Controller"])