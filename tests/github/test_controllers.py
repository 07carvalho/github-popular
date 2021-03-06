from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app


@patch("app.github.clients.GitHubRequestClient.get_repo")
def test_popular_repo(requests_get, popular_repo, is_popular):
    with TestClient(app) as client:
        requests_get.return_value = (popular_repo, 200)

        url = "/github/repos/pytest-dev/pytest/popularity"
        response = client.get(url)

        assert response.json() == is_popular
        requests_get.assert_called_once_with("pytest-dev", "pytest")


@patch("app.github.clients.GitHubRequestClient.get_repo")
def test_unpopular_repo(requests_get, unpopular_repo, unpopular):
    with TestClient(app) as client:
        requests_get.return_value = (unpopular_repo, 200)

        url = "/github/repos/07carvalho/delivery/popularity"
        response = client.get(url)

        assert response.json() == unpopular
        requests_get.assert_called_once_with("07carvalho", "delivery")


@patch("app.github.clients.GitHubRequestClient.get_repo")
def test_request_http_error(requests_get, not_found_response, error_response):
    with TestClient(app) as client:
        requests_get.return_value = (not_found_response, 404)

        url = "/github/repos/pytest-dev/pyt/popularity"
        response = client.get(url)

        assert response.json() == error_response
        requests_get.assert_called_once_with("pytest-dev", "pyt")
