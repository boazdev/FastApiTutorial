from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_login_exist(): #username and password are correct
    obj={"username": "test_user", "password": "test123"}
    response = client.post("/auth/login", data=obj)
    tokens = response.json()
    assert response.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]
    #return tokens["access_token"]

def test_login_not_exist():
    obj={"username": "doesnt_exist", "password": "test123"}
    response = client.post("/auth/login", data=obj)
    assert response.status_code == 400
    assert response.json() == {
  "detail": "Incorrect username"
}
    

    
def test_incorrect_pass():
    obj={"username": "test_user", "password": "test1234"}
    response = client.post("/auth/login", data=obj)
    assert response.status_code == 400
    assert response.json() == {
  "detail": "Incorrect password"
    }

def test_use_access_token(): #username and password are correct
    obj={"username": "test_user", "password": "test123"}
    response = client.post("/auth/login", data=obj)
    token = response.json()
    assert response.status_code == 200
    assert "access_token" in token
    assert token["access_token"]
    response = client.get("/employee/",headers={"Authorization": "Bearer " + token["access_token"]})
    assert response.status_code == 200

def test_use_no_token():
    response = client.get("/employee/")
    assert response.status_code == 401

def test_use_bad_token():
    dummy_token = "jadjasdjiafja893wth"
    response = client.get("/employee/",headers={"Authorization": "Bearer " + dummy_token})
    assert response.status_code == 403