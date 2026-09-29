from fastapi import APIRouter, Depends

from app.jobs.models import Job
from app.jobs.repository import JobRepository
from app.jobs.schemas import JobResponse
from app.jobs.service import JobService

router = APIRouter(prefix="/jobs", tags=["jobs"])

repository = JobRepository()


def get_job_repository() -> JobRepository:
    return repository


def get_job_service(
    job_repository: JobRepository = Depends(get_job_repository),  # noqa: B008
) -> JobService:
    return JobService(job_repository)


@router.get("/", response_model=list[JobResponse])
async def list_jobs(
    service: JobService = Depends(get_job_service),  # noqa: B008
) -> list[Job]:
    return service.get_jobs()