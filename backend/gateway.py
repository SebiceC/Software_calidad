from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

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

# ---- Rutas para Matrices de Mitigación ----
@app.route('/mitigation_matrices/<int:matrix_id>', methods=['GET'])
def get_mitigation_matrix_details(matrix_id):
    """Redirige una solicitud GET para obtener una matriz de mitigación específica."""
    try:
        response = requests.get(f"{MICROSERVICE1_BASE_URL}/mitigation_matrices/{matrix_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/mitigation_matrices', methods=['POST'])
def create_mitigation_matrix():
    """Redirige una solicitud POST para crear una nueva matriz de mitigación."""
    data = request.json
    try:
        response = requests.post(f"{MICROSERVICE1_BASE_URL}/mitigation_matrices", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# ---- Rutas para Matrices de Riesgo ----
@app.route('/risk_matrices', methods=['GET'])
def get_risk_matrices():
    """Redirige una solicitud GET para obtener todas las matrices de riesgo."""
    try:
        response = requests.get(f"{MICROSERVICE1_BASE_URL}/risk_matrices")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/risk_matrices/<int:matrix_id>', methods=['GET'])
def get_risk_matrix_details(matrix_id):
    """Redirige una solicitud GET para obtener los detalles de una matriz de riesgo por ID."""
    try:
        response = requests.get(f"{MICROSERVICE1_BASE_URL}/risk_matrices/{matrix_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/risk_matrices', methods=['POST'])
def create_risk_matrix():
    """Redirige una solicitud POST para crear una nueva matriz de riesgo."""
    data = request.json
    try:
        response = requests.post(f"{MICROSERVICE1_BASE_URL}/risk_matrices", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/risk_matrices/<int:matrix_id>', methods=['DELETE'])
def delete_risk_matrix(matrix_id):
    """Redirige una solicitud DELETE para eliminar una matriz de riesgo por ID."""
    try:
        response = requests.delete(f"{MICROSERVICE1_BASE_URL}/risk_matrices/{matrix_id}")
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
