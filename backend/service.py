from flask import jsonify
from model import (
    get_all_users_db,
    create_user_db,
    update_user_db,
    delete_user_db,
    get_all_companies_db,
    create_company_db,
    get_all_evaluations_db,
    create_evaluation_db,
)

# ---- Funciones para Usuarios ----

def get_all_users_service():
    """Servicio para obtener todos los usuarios."""
    try:
        users = get_all_users_db()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": f"Error al recuperar usuarios: {str(e)}"}), 500


def create_user_service(data):
    """Servicio para crear un nuevo usuario."""
    try:
        required_fields = ["nombre", "correo", "contraseña", "rol"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo faltante: {field}"}), 400

        if data["rol"] not in ["Usuario", "Administrador"]:
            return jsonify({"error": "rol no válido. Permitido: 'Usuario', 'Administrador'"}), 400

        new_user = create_user_db(data)
        return jsonify({"message": "Usuario creado satisfactoriamente", "user": new_user}), 201
    except Exception as e:
        return jsonify({"error": f"Error creando usuario: {str(e)}"}), 500


def update_user_service(user_id, data):
    """Servicio para actualizar un usuario."""
    try:
        updated_user = update_user_db(user_id, data)
        if updated_user:
            return jsonify({"message": "Usuario actualizado satisfactoriamente", "user": updated_user}), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Error al actualizar el usuario: {str(e)}"}), 500


def delete_user_service(user_id):
    """Servicio para eliminar un usuario."""
    try:
        result = delete_user_db(user_id)
        if result:
            return jsonify({"message": "Usuario eliminado satisfactoriamente"}), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Error al eliminar usuario: {str(e)}"}), 500


# ---- Funciones para Empresas ----

def get_all_companies_service():
    """Servicio para obtener todas las empresas."""
    try:
        companies = get_all_companies_db()
        return jsonify(companies), 200
    except Exception as e:
        return jsonify({"error": f"Error al obtener empresa: {str(e)}"}), 500


def create_company_service(data):
    """Servicio para crear una nueva empresa."""
    try:
        required_fields = ["nombre", "direccion", "sector"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo faltante: {field}"}), 400

        new_company = create_company_db(data)
        return jsonify({"message": "Empresa creada satisfactoriamente", "company": new_company}), 201
    except Exception as e:
        return jsonify({"error": f"Error al crear la empresa: {str(e)}"}), 500


# ---- Funciones para Evaluaciones ----

def get_all_evaluations_service():
    """Servicio para obtener todas las evaluaciones."""
    try:
        evaluations = get_all_evaluations_db()
        return jsonify(evaluations), 200
    except Exception as e:
        return jsonify({"error": f"Error al obtener evaluaciones: {str(e)}"}), 500


def create_evaluation_service(data):
    """Servicio para crear una nueva evaluación."""
    try:
        required_fields = ["id_empresa", "id_usuario", "puntaje_total", "porcentaje_total", "resultado"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo faltante: {field}"}), 400

        new_evaluation = create_evaluation_db(data)
        return jsonify({"message": "Evaluacion creada satisfactoriamente", "evaluation": new_evaluation}), 201
    except Exception as e:
        return jsonify({"error": f"Error al crear la evaluacion: {str(e)}"}), 500
