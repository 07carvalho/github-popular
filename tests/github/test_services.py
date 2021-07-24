from app.github.services import GitHubService


def test_repo_is_popular():
    assert GitHubService.repo_is_popular(500, 1)


def test_repo_is_popular2():
    assert GitHubService.repo_is_popular(0, 250)


def test_repo_unpopular():
    assert not GitHubService.repo_is_popular(0, 1)


def test_repo_unpopular2():
    assert not GitHubService.repo_is_popular(499, 0)
