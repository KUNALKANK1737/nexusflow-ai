from app.jobs.models import Job
from app.jobs.repository import JobRepository


def test_add_and_get_jobs() -> None:
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

    jobs = repository.get_all()

    assert len(jobs) == 1
    assert jobs[0] == job