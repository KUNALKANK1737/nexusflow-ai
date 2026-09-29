from app.jobs.models import Job
from app.jobs.repository import JobRepository


class JobService:
    def __init__(self, repository: JobRepository) -> None:
        self.repository = repository

    def get_jobs(self) -> list[Job]:
        return self.repository.get_all()