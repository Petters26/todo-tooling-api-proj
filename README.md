# Tasks API - Tooling Project

REST microservice for task management (To-Do list) built with **Flask**.
The focus of the project is mastering professional Python *tooling*:
virtual environments, package management, linters, formatters, and version
control with Git.

## Team members

- Name 1
- Name 2
- Name 3

> ⚠️ Replace the names above with the actual team members.

## Installation and running

```bash
# Clone repository
git clone <repo-url>
cd <repo-name>

# Create virtual environment
python -m venv .venv

# Activate environment
# Windows (PowerShell / CMD):
.venv\Scripts\activate
# Windows (Git Bash):
source .venv/Scripts/activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server (port 5000)
python app.py
```

The server listens on **http://127.0.0.1:5000**.

## Tooling commands

```bash
# Style linter (PEP8) — must not show warnings
flake8 app.py

# Formatter — formats the code
black app.py
# Check formatting without modifying (used during the defense)
black --check app.py

# Quality linter — must score >= 8.0/10
pylint app.py
```

> The Flake8 configuration lives in `setup.cfg` (line length aligned with
> Black at 88 columns) and the Pylint one in `.pylintrc` (custom team
> rules).

## Tests (bonus)

```bash
# Run the test suite from the project root
pytest -v
```

## Endpoints

| Method | Path             | Description            | Successful response |
|--------|------------------|------------------------|---------------------|
| GET    | `/tasks`         | List all tasks         | `200` + JSON list |
| POST   | `/tasks`         | Create a new task      | `201` + created task |
| DELETE | `/tasks/<id>`    | Delete a task          | `200` (or `404` if not found) |

### Usage examples

```bash
# List tasks
curl http://127.0.0.1:5000/tasks

# Create a task (valid JSON)
curl -X POST http://127.0.0.1:5000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title": "Learn Flask"}'

# Create without title -> 400
curl -X POST http://127.0.0.1:5000/tasks \
     -H "Content-Type: application/json" -d '{}'

# Delete the task with id 1
curl -X DELETE http://127.0.0.1:5000/tasks/1
```
