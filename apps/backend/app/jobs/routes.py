from fastapi import APIRouter, Depends

from app.jobs.models import Job
from app.jobs.repository import JobRepository
from app.jobs.schemas import JobResponse

router = APIRouter(prefix="/jobs", tags=["jobs"])

repository = JobRepository()


def get_job_repository() -> JobRepository:
    return repository


@router.get("/", response_model=list[JobResponse])
async def list_jobs(
    job_repository: JobRepository = Depends(get_job_repository),  # noqa: B008
) -> list[Job]:
    return job_repository.get_all()