from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_popular_repo(healthy_response):
    response = client.get("/healthz")

    assert response.json() == healthy_response
