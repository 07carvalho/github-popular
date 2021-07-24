from app.github.enums import GitHubRepoEnum


class GitHubService:
    @staticmethod
    def repo_is_popular(stargazers_count: int, forks_count: int) -> bool:
        score = stargazers_count + (forks_count * 2)
        return score >= GitHubRepoEnum.POPULAR_SCORE.value
