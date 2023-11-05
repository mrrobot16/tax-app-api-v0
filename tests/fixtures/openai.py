import pytest

from app.services.openai import OpenAIService

@pytest.fixture
def openai_service():
    service = OpenAIService()
    yield service