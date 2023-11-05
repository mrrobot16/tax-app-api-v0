import pytest

from app.services.openai import OpenAIService

@pytest.fixture
def openai_service():
    # Setup code
    service = OpenAIService()
    yield service