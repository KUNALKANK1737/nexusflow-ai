from app.jobs.models import Job


class JobRepository:
    def __init__(self) -> None:
        self._jobs: list[Job] = []

    def get_all(self) -> list[Job]:
        return self._jobs

    def add(self, job: Job) -> Job:
        self._jobs.append(job)
        return job