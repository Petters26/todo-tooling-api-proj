from flask import Flask, jsonify, request

app = Flask(__name__)

tareas = [
    {"id": 1, "titulo": "Aprender Flask", "completada": False},
    {"id": 2, "titulo": "Dominar el Tooling", "completada": False}
]

@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    pass

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    pass

@app.route('/tareas/<int:id_tarea>', methods=['DELETE'])
def eliminar_tarea(id_tarea):
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)