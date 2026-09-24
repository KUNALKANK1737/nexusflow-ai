from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.jobs.routes import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_list_jobs():
    response = client.get("/jobs/")

    assert response.status_code == 200
    assert response.json() == []