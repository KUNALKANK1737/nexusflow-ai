from pydantic import BaseModel, HttpUrl


class JobResponse(BaseModel):
    title: str
    company: str
    location: str
    description: str
    source: str
    url: HttpUrl