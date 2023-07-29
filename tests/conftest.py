import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from typing import Generator,Dict

#from app.db.session import SessionLocal
from main import app

@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="module")
def get_token_header(client: TestClient) -> Dict[str, str]:
    obj={"username": "test_user", "password": "test123"}
    response = client.post("/auth/login", data=obj)
    token_data = response.json()
    token_header = {"Authorization": "Bearer " + token_data["access_token"]}
    return token_header


