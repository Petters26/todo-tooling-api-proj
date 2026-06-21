# API de Tareas - Proyecto Tooling

Microservicio REST de gestión de tareas (To-Do list) construido con **Flask**.
El foco del proyecto es el dominio del *tooling* profesional de Python:
entornos virtuales, gestión de paquetes, linters, formatters y control de
versiones con Git.

## Integrantes del equipo

- Nombre 1
- Nombre 2
- Nombre 3

> ⚠️ Reemplaza los nombres anteriores por los integrantes reales del equipo.

## Instalación y ejecución

```bash
# Clonar repositorio
git clone <url-del-repo>
cd <nombre-del-repo>

# Crear entorno virtual
python -m venv .venv

# Activar entorno
# Windows (PowerShell / CMD):
.venv\Scripts\activate
# Windows (Git Bash):
source .venv/Scripts/activate
# Mac/Linux:
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor (puerto 5000)
python app.py
```

El servidor queda escuchando en **http://127.0.0.1:5000**.

## Comandos de tooling

```bash
# Linter de estilo (PEP8) — no debe mostrar advertencias
flake8 app.py

# Formatter — formatea el código
black app.py
# Verificar formato sin modificar (se usa en la defensa)
black --check app.py

# Linter de calidad — debe dar una puntuación >= 8.0/10
pylint app.py
```

> La configuración de Flake8 vive en `setup.cfg` (longitud de línea alineada
> con Black en 88 columnas) y la de Pylint en `.pylintrc` (reglas
> personalizadas del equipo).

## Pruebas (bono)

```bash
# Ejecutar la suite de pruebas desde la raíz del proyecto
pytest -v
```

## Endpoints

| Método | Ruta             | Descripción            | Respuesta exitosa |
|--------|------------------|------------------------|-------------------|
| GET    | `/tasks`         | Listar todas las tareas| `200` + lista JSON |
| POST   | `/tasks`         | Crear una nueva tarea  | `201` + tarea creada |
| DELETE | `/tasks/<id>`    | Eliminar una tarea     | `200` (o `404` si no existe) |

### Ejemplos de uso

```bash
# Listar tareas
curl http://127.0.0.1:5000/tasks

# Crear una tarea (JSON válido)
curl -X POST http://127.0.0.1:5000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title": "Learn Flask"}'

# Crear sin title -> 400
curl -X POST http://127.0.0.1:5000/tasks \
     -H "Content-Type: application/json" -d '{}'

# Eliminar la tarea con id 1
curl -X DELETE http://127.0.0.1:5000/tasks/1
```
