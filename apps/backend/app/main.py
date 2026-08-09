from fastapi import FastAPI

from app.api.routes.health import router as health_router

app = FastAPI(
    title="NexusFlow AI",
    description="AI-powered career intelligence platform",
    version="0.1.0",
)

app.include_router(health_router)