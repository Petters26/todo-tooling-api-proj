"""REST API for Tasks built with Flask.

Exposes endpoints to list, create, and delete tasks, along with
global error handlers (400/404/500) responding in JSON.
"""

from flask import Flask, jsonify, request, abort


app = Flask(__name__)


tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Master Tooling", "completed": False},
]


@app.errorhandler(400)
def bad_request(error):
    """Respond 400 in JSON when the request is invalid."""
    return (
        jsonify(
            {
                "error": "Bad request",
                "message": (
                    "The request body is not a valid JSON or "
                    "lacks the required fields."
                ),
            }
        ),
        400,
    )


@app.errorhandler(404)
def resource_not_found(error):
    """Respond 404 in JSON when the resource or route does not exist."""
    return (
        jsonify(
            {
                "error": "Resource not found",
                "message": (
                    "The requested URL or resource was not found on "
                    "this server."
                ),
            }
        ),
        404,
    )


@app.errorhandler(500)
def internal_server_error(error):
    """Respond 500 in JSON upon an unexpected server error."""
    return (
        jsonify(
            {
                "error": "Internal server error",
                "message": (
                    "An unexpected error occurred in our system. "
                    "Please try again later."
                ),
            }
        ),
        500,
    )


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """Return the complete list of tasks with code 200."""
    return jsonify(tasks), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    """Create a task from received JSON and return it with 201.
    If the 'title' field is missing or JSON is invalid, responds with 400.
    """
    data = request.get_json(silent=True)
    if not data or not data.get("title"):
        abort(400)
    new_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id": new_id,
        "title": data["title"],
        "completed": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete the task with the given ID (200) or responds 404 if not found."""
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        abort(404)
    tasks.remove(task)
    return jsonify({"message": f"Task {task_id} deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)