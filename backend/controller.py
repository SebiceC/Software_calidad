from flask import Blueprint, request, jsonify, send_file
from service import (
    get_all_users_service,
    create_user_service,
    update_user_service,
    delete_user_service,
    login_service,
    get_criteria_by_norms_service,
    get_all_companies_service,
    create_company_service,
    get_all_evaluations_service,
    create_evaluation_service,
    generate_evaluation_pdf,
    get_all_risk_matrices_service, 
    create_risk_matrix_service,     
    delete_risk_matrix_service,
    create_mitigation_matrix_service     
)

controller = Blueprint('controller', __name__)

# ---- Rutas para Usuarios ----
@controller.route('/users', methods=['GET'])
def get_users():
    return get_all_users_service()

# Ruta para iniciar sesión
@controller.route('/login', methods=['POST'])
def login():
    data = request.form  
    user_data = {
        "correo": data.get("correo"),
        "contraseña": data.get("contraseña")
    }
    return login_service(user_data)

@controller.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_data = {
        "nombre": data.get("nombre"),
        "correo": data.get("correo"),
        "contraseña": data.get("contraseña"),
        "rol": data.get("rol")
    }
    return create_user_service(data)

@controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    return update_user_service(user_id, data)

@controller.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete_user_service(user_id)

@controller.route('/criterios', methods=['GET'])
def get_criteria_by_norms():
    """Ruta para obtener criterios por normas y ordenados por porcentaje."""
    norms = request.args.getlist('normas')  # Captura normas como lista de parámetros
    return get_criteria_by_norms_service(norms)

# ---- Rutas para Empresas ----
@controller.route('/companies', methods=['GET'])
def get_companies():
    return get_all_companies_service()

@controller.route('/companies', methods=['POST'])
def create_company():
    data = request.json
    company_data = {
        "nombre": data.get("nombre"),
        "direccion": data.get("direccion"),
        "sector": data.get("sector")
    }
    return create_company_service(data)

# ---- Rutas para Evaluaciones ----
@controller.route('/evaluations', methods=['GET'])
def get_evaluations():
    return get_all_evaluations_service()

@controller.route('/evaluations', methods=['POST'])
def submit_evaluation():
    """Ruta para enviar una evaluación de software."""
    data = request.json
    return create_evaluation_service(data)

@controller.route('/evaluations/<int:evaluation_id>/download', methods=['GET'])
def download_evaluation_pdf(evaluation_id):
    """Genera y permite la descarga del PDF de una evaluación."""
    try:
        pdf_file_path = generate_evaluation_pdf(evaluation_id)
        return send_file(pdf_file_path, as_attachment=True)
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# ---- Rutas para Matrices de Riesgo ----

@controller.route('/risk_matrices', methods=['GET'])
def get_risk_matrices():
    """Ruta para obtener todas las matrices de riesgo."""
    try:
        return get_all_risk_matrices_service()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/risk_matrices', methods=['POST'])
def create_risk_matrix():
    """Ruta para crear una nueva matriz de riesgo."""
    data = request.json
    try:
        return create_risk_matrix_service(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/risk_matrices/<int:matrix_id>', methods=['DELETE'])
def delete_risk_matrix(matrix_id):
    """Ruta para eliminar una matriz de riesgo por ID."""
    try:
        return delete_risk_matrix_service(matrix_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@controller.route('/mitigation_matrices', methods=['POST'])
def create_mitigation_matrix():
    """Crea una matriz de mitigación."""
    try:
        data = request.json
        mitigation_id = create_mitigation_matrix_service(data)
        return jsonify({"message": "Matriz de mitigación creada con éxito", "id_matriz_mitig": mitigation_id}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"Error al crear la matriz de mitigación: {str(e)}"}), 500
