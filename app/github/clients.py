import os

import aiohttp
from aiohttp import web


class GitHubRequestClient:
    base_url = "https://api.github.com"

    def __init__(self):
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"Token {os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')}",
        }

    async def get_repo(self, owner: str, repo: str):
        url = f"{self.base_url}/repos/{owner}/{repo}"
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url) as response:
                try:
                    return await response.json(), response.status
                except web.HTTPException:
                    return await response.json(), response.status
                except Exception:
                    msg = "Sorry, something is wrong. Try again later."
                    return {"message": msg}, response.status
