import pytest


@pytest.fixture
def popular_repo():
    return {
        "stargazers_count": 500,
        "forks_count": 200,
    }


@pytest.fixture
def unpopular_repo():
    return {
        "stargazers_count": 5,
        "forks_count": 0,
    }


@pytest.fixture
def not_found_response():
    return {
        "message": "Not Found",
        "documentation_url": "https://docs.github.com/rest/reference/repos#get-a-repository",
    }


@pytest.fixture
def is_popular():
    return {"popular": True}


@pytest.fixture
def unpopular():
    return {"popular": False}


@pytest.fixture
def error_response():
    return {"detail": "Not Found"}
