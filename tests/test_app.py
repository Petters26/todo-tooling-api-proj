"""Suite de pruebas (pytest) para la API de Tareas.

Verifica los endpoints GET, POST y DELETE de /tasks con el cliente de
pruebas de Flask, sin necesidad de levantar el servidor.
"""

import pytest

from app import app


@pytest.fixture
def client():
    """Cliente de pruebas de Flask en modo testing."""
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_list_tasks_returns_200(client):
    """Listar tareas responde 200 y una lista JSON."""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_create_task_success_returns_201(client):
    """Crear una tarea con datos válidos responde 201."""
    response = client.post("/tasks", json={"title": "Test the API"})
    assert response.status_code == 201
    body = response.get_json()
    assert body["title"] == "Test the API"
    assert "id" in body


def test_create_task_without_title_returns_400(client):
    """Crear una tarea sin título responde 400."""
    response = client.post("/tasks", json={})
    assert response.status_code == 400


def test_delete_existing_task_returns_200(client):
    """Eliminar una tarea existente responde 200."""
    created = client.post("/tasks", json={"title": "Task to delete"})
    created_id = created.get_json()["id"]
    response = client.delete(f"/tasks/{created_id}")
    assert response.status_code == 200


def test_delete_missing_task_returns_404(client):
    """Eliminar una tarea inexistente responde 404."""
    response = client.delete("/tasks/999999")
    assert response.status_code == 404


def test_unknown_route_returns_404(client):
    """Una ruta no registrada activa el manejador global 404."""
    response = client.get("/route-that-does-not-exist")
    assert response.status_code == 404
    assert "error" in response.get_json()
