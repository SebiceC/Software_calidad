from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Base URL del microservicio 1
MICROSERVICE1_BASE_URL = "http://localhost:5000/microservice1"

# ---- Rutas para Usuarios ----

@app.route('/users', methods=['GET'])
def get_users():
    """Redirige una solicitud GET para obtener todos los usuarios."""
    try:
        response = requests.get(f"{MICROSERVICE1_BASE_URL}/users")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users', methods=['POST'])
def create_user():
    """Redirige una solicitud POST para crear un nuevo usuario."""
    data = request.json
    try:
        response = requests.post(f"{MICROSERVICE1_BASE_URL}/users", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Redirige una solicitud PUT para actualizar un usuario."""
    data = request.json
    try:
        response = requests.put(f"{MICROSERVICE1_BASE_URL}/users/{user_id}", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Redirige una solicitud DELETE para eliminar un usuario."""
    try:
        response = requests.delete(f"{MICROSERVICE1_BASE_URL}/users/{user_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


# ---- Rutas para Empresas ----

@app.route('/companies', methods=['GET'])
def get_companies():
    """Redirige una solicitud GET para obtener todas las empresas."""
    try:
        response = requests.get(f"{MICROSERVICE1_BASE_URL}/companies")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/companies', methods=['POST'])
def create_company():
    """Redirige una solicitud POST para crear una nueva empresa."""
    data = request.json
    try:
        response = requests.post(f"{MICROSERVICE1_BASE_URL}/companies", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


# ---- Rutas para Evaluaciones ----

@app.route('/evaluations', methods=['GET'])
def get_evaluations():
    """Redirige una solicitud GET para obtener todas las evaluaciones."""
    try:
        response = requests.get(f"{MICROSERVICE1_BASE_URL}/evaluations")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/evaluations', methods=['POST'])
def create_evaluation():
    """Redirige una solicitud POST para crear una nueva evaluación."""
    data = request.json
    try:
        response = requests.post(f"{MICROSERVICE1_BASE_URL}/evaluations", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


# ---- Manejo de errores global ----

@app.errorhandler(404)
def not_found_error(error):
    """Manejador global para errores 404."""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Manejador global para errores 500."""
    return jsonify({"error": "Internal server error"}), 500


# ---- Iniciar el Gateway ----

if __name__ == '__main__':
    app.run(debug=True, port=8000)