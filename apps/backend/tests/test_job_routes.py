from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.jobs.models import Job
from app.jobs.repository import JobRepository
from app.jobs.routes import get_job_repository, router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_list_jobs() -> None:
    response = client.get("/jobs/")

    assert response.status_code == 200
    assert response.json() == []


def test_list_jobs_returns_stored_job() -> None:
    repository = JobRepository()

    job = Job(
        title="Data Scientist",
        company="Example Company",
        location="Pune, India",
        description="Build machine learning solutions.",
        source="LinkedIn",
        url="https://www.linkedin.com/jobs/view/123456789",
    )

    repository.add(job)

    app.dependency_overrides[get_job_repository] = lambda: repository

    try:
        response = client.get("/jobs/")

        assert response.status_code == 200
        assert response.json() == [
            {
                "title": "Data Scientist",
                "company": "Example Company",
                "location": "Pune, India",
                "description": "Build machine learning solutions.",
                "source": "LinkedIn",
                "url": "https://www.linkedin.com/jobs/view/123456789",
            }
        ]
    finally:
        app.dependency_overrides.clear()