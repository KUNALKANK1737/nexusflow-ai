from app.jobs.models import Job
from app.jobs.repository import JobRepository
from app.jobs.service import JobService


def test_get_jobs() -> None:
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

    service = JobService(repository)

    jobs = service.get_jobs()

    assert jobs == [job]