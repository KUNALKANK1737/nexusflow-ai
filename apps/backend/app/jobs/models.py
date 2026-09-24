from pydantic import BaseModel, HttpUrl


class Job(BaseModel):
    title: str
    company: str
    location: str
    description: str
    source: str
    url: HttpUrl