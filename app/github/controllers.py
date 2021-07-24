from fastapi import APIRouter, HTTPException

from app.github.clients import GitHubRequestClient
from app.github.schemas import ErrorResponse, SuccessPopularityResponse
from app.github.services import GitHubService

router = APIRouter()


@router.get(
    "/repos/{owner}/{repo}/popularity",
    response_model=SuccessPopularityResponse,
    responses={404: {"model": ErrorResponse}},
)
async def repo_popularity(owner: str, repo: str):
    data, status = await GitHubRequestClient().get_repo(owner, repo)
    if status != 200:
        raise HTTPException(status_code=status, detail=data.get("message"))
    stargazers_count = data["stargazers_count"]
    forks_count = data["forks_count"]
    popularity = GitHubService.repo_is_popular(stargazers_count, forks_count)
    return {"popular": popularity}
