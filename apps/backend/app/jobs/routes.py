from fastapi import APIRouter

from app.jobs.schemas import JobResponse

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/", response_model=list[JobResponse])
async def list_jobs() -> list[JobResponse]:
    return []