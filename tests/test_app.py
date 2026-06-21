"""Test suite (pytest) for the Tasks API.

Verifies the GET, POST, and DELETE endpoints of /tasks using Flask's
test client, without needing to start the server.
"""

import pytest

from app import app


@pytest.fixture
def client():
    """Flask test client in testing mode."""
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_list_tasks_returns_200(client):
    """Listing tasks responds 200 and a JSON list."""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_create_task_success_returns_201(client):
    """Creating a task with valid data responds 201."""
    response = client.post("/tasks", json={"title": "Test the API"})
    assert response.status_code == 201
    body = response.get_json()
    assert body["title"] == "Test the API"
    assert "id" in body


def test_create_task_without_title_returns_400(client):
    """Creating a task without a title responds 400."""
    response = client.post("/tasks", json={})
    assert response.status_code == 400


def test_delete_existing_task_returns_200(client):
    """Deleting an existing task responds 200."""
    created = client.post("/tasks", json={"title": "Task to delete"})
    created_id = created.get_json()["id"]
    response = client.delete(f"/tasks/{created_id}")
    assert response.status_code == 200


def test_delete_missing_task_returns_404(client):
    """Deleting a non-existent task responds 404."""
    response = client.delete("/tasks/999999")
    assert response.status_code == 404


def test_unknown_route_returns_404(client):
    """An unregistered route triggers the global 404 handler."""
    response = client.get("/route-that-does-not-exist")
    assert response.status_code == 404
    assert "error" in response.get_json()
