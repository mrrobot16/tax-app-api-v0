from fastapi import FastAPI

from app.controllers.openai import openai_controller

def configure_routes(app: FastAPI):
    app.include_router(openai_controller, prefix="/openai", tags=["OpenAI Controller"])