from fastapi import APIRouter, HTTPException
from fastapi_cache.decorator import cache

from app.github.clients import GitHubRequestClient
from app.github.schemas import ErrorResponse, SuccessPopularityResponse
from app.github.services import GitHubService
from app.handlers.key_builder import custom_key_builder

router = APIRouter()


@router.get(
    "/repos/{owner}/{repo}/popularity",
    response_model=SuccessPopularityResponse,
    responses={404: {"model": ErrorResponse}},
)
@cache(namespace="github", expire=3600, key_builder=custom_key_builder)
async def repo_popularity(owner: str, repo: str):
    data, status = await GitHubRequestClient().get_repo(owner, repo)
    if status != 200:
        raise HTTPException(status_code=status, detail=data.get("message"))
    stargazers_count = data["stargazers_count"]
    forks_count = data["forks_count"]
    popularity = GitHubService.repo_is_popular(stargazers_count, forks_count)
    return {"popular": popularity}
