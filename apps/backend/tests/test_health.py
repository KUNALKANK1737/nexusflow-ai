from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "nexusflow-api",
    }


def test_list_jobs() -> None:
    response = client.get("/jobs/")

    assert response.status_code == 200
    assert response.json() == []