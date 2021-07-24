from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from app.github.controllers import router as github_router
from app.schemas import HealthCheckResponse

app = FastAPI()


@app.get("/healthz", response_model=HealthCheckResponse)
async def health_check():
    return {"result": "OK - healthy"}


app.include_router(github_router, prefix="/github", tags=["github"])


@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
