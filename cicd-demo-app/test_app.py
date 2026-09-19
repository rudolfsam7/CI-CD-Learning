from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home_page():
    response = client.get("/")

    assert response.status_code == 200
    assert "Just Checking......" in response.text


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200


def test_health_status():
    response = client.get("/health")

    assert response.json() == {"status": "healthy"}
