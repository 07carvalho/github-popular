from fastapi import FastAPI

from app.github.controllers import router as github_router

app = FastAPI()
app.include_router(github_router, prefix="/github", tags=["github"])
