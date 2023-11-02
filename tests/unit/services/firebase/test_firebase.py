from fastapi.testclient import TestClient
from db.firebase import FIREBASE_CREDENTIALS

def test_health():
    assert type(FIREBASE_CREDENTIALS['type'])  == str
