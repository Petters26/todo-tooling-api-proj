from flask import Flask, jsonify, request

app = Flask(__name__)

tareas = [
    {"id": 1, "titulo": "Aprender Flask", "completada": False},
    {"id": 2, "titulo": "Dominar el Tooling", "completada": False}
]

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


@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify(tareas), 200

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    return jsonify({"mensaje": "Endpoint POST listo para ser implementado por Dev 3"}), 200

@app.route('/tareas/<int:id_tarea>', methods=['DELETE'])
def eliminar_tarea(id_tarea):
    return jsonify({"mensaje": f"Endpoint DELETE para ID {id_tarea} listo para ser implementado por Dev 3"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)