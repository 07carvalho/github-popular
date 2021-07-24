from fastapi import FastAPI

from app.github.controllers import router as github_router
from app.schemas import HealthCheckResponse

app = FastAPI()


@app.get("/healthz", response_model=HealthCheckResponse)
async def health_check():
    return {"result": "OK - healthy"}


app.include_router(github_router, prefix="/github", tags=["github"])
