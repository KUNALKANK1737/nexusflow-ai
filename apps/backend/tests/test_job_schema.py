from app.jobs.schemas import JobResponse


def test_job_response_schema():
    job = JobResponse(
        title="Data Scientist",
        company="Example Company",
        location="Pune, India",
        description="Build machine learning solutions.",
        source="LinkedIn",
        url="https://www.linkedin.com/jobs/view/123456789",
    )

    assert job.title == "Data Scientist"
    assert job.company == "Example Company"
    assert job.location == "Pune, India"
    assert job.source == "LinkedIn"