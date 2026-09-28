from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_homepage() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "EduGenie" in response.text


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
