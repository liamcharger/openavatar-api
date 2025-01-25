from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"email": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_get_user():
    # First create a user, then retrieve it
    create_response = client.post("/users/", json={"email": "test@example.com", "password": "testpassword"})
    user_id = create_response.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"