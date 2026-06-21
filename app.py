from flask import Flask, jsonify, request, abort


app = Flask(__name__)


tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Master Tooling", "completed": False},
]


@app.errorhandler(400)
def peticion_incorrecta(error):
    return jsonify({
        "error": "Petición incorrecta",
        "mensaje": "El cuerpo de la solicitud no es un JSON válido o carece de los campos requeridos."
    }), 400

@app.errorhandler(404)
def recurso_no_encontrado(error):
    return jsonify({
        "error": "Recurso no encontrado",
        "mensaje": "La ruta solicitada o el recurso no existe en este servidor."
    }), 404

@app.errorhandler(500)
def error_interno_servidor(error):
    return jsonify({
        "error": "Error interno del servidor",
        "mensaje": "Ha ocurrido un error inesperado en nuestro sistema. Por favor, inténtelo de nuevo más tarde."
    }), 500


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