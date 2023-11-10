# fixtures/tasks.py
import pytest
from fastapi import BackgroundTasks

@pytest.fixture
def tasks():
    class TestBackgroundTasks(BackgroundTasks):
        def add_task(self, func, *args, **kwargs):
            # Run the task immediately instead of in the background
            func(*args, **kwargs)

    return TestBackgroundTasks()