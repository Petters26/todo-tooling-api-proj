"""Suite de pruebas (pytest) para la API de Tareas.

Estas pruebas funcionan como CONTRATO de los endpoints que implementa Dev 3.
Verifican GET, POST y DELETE sobre /tareas usando el test_client() de Flask,
por lo que NO requieren levantar el servidor en el puerto 5000.

Ejecutar desde la raiz del proyecto con el entorno virtual activo:

    pytest -v
"""

import pytest

from app import app, tareas


@pytest.fixture
def cliente():
    """Cliente de pruebas de Flask en modo testing."""
    app.config["TESTING"] = True
    with app.test_client() as cliente_prueba:
        yield cliente_prueba


# --- GET /tareas -----------------------------------------------------------
def test_listar_tareas_devuelve_200(cliente):
    """GET /tareas debe responder 200 y una lista JSON."""
    respuesta = cliente.get("/tareas")
    assert respuesta.status_code == 200
    assert isinstance(respuesta.get_json(), list)


# --- POST /tareas ----------------------------------------------------------
def test_crear_tarea_exitosa_devuelve_201(cliente):
    """POST con un titulo valido debe crear la tarea y responder 201."""
    respuesta = cliente.post("/tareas", json={"titulo": "Probar la API"})
    assert respuesta.status_code == 201
    cuerpo = respuesta.get_json()
    assert cuerpo["titulo"] == "Probar la API"
    assert "id" in cuerpo


def test_crear_tarea_sin_titulo_devuelve_400(cliente):
    """POST sin el campo 'titulo' debe responder 400 (peticion incorrecta)."""
    respuesta = cliente.post("/tareas", json={})
    assert respuesta.status_code == 400


# --- DELETE /tareas/<id> ---------------------------------------------------
def test_eliminar_tarea_existente_devuelve_200(cliente):
    """DELETE de una tarea recien creada debe responder 200."""
    creada = cliente.post("/tareas", json={"titulo": "Tarea a eliminar"})
    id_creado = creada.get_json()["id"]
    respuesta = cliente.delete(f"/tareas/{id_creado}")
    assert respuesta.status_code == 200


def test_eliminar_tarea_inexistente_devuelve_404(cliente):
    """DELETE de un id que no existe debe responder 404."""
    respuesta = cliente.delete("/tareas/999999")
    assert respuesta.status_code == 404


# --- Manejo global de errores (Dev 1) --------------------------------------
def test_ruta_inexistente_devuelve_404(cliente):
    """Una ruta no registrada debe activar el manejador global 404."""
    respuesta = cliente.get("/ruta-que-no-existe")
    assert respuesta.status_code == 404
    assert "error" in respuesta.get_json()
