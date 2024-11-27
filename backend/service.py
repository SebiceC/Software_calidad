from flask import jsonify
from fpdf import FPDF
from model import (
    get_all_users_db,
    create_user_db,
    update_user_db,
    delete_user_db,
    get_user_by_email_db,
    get_criteria_by_norms_db,
    get_all_companies_db,
    create_company_db,
    get_all_evaluations_db,
    create_evaluation_db,
    get_evaluation_details
)
from bcrypt import checkpw

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
    
def login_service(data):
    """Servicio para manejar el inicio de sesión."""
    try:
        required_fields = ["correo", "contraseña"]
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Obtener el usuario de la base de datos por correo
        user = get_user_by_email_db(data["correo"])
        if not user:
            return jsonify({"error": "Invalid email or password"}), 401

        # Verificar la contraseña
        if not checkpw(data["contraseña"].encode('utf-8'), user["contraseña"].encode('utf-8')):
            return jsonify({"error": "Invalid email or password"}), 401

        # Respuesta exitosa con detalles del usuario (sin incluir la contraseña)
        return jsonify({
            "message": "Login successful",
            "user": {
                "id_usuario": user["id_usuario"],
                "nombre": user["nombre"],
                "correo": user["correo"],
                "rol": user["rol"]
            }
        }), 200
    except Exception as e:
        return jsonify({"error": f"Error during login: {str(e)}"}), 500
    
def get_criteria_by_norms_service(norms):
    """Servicio para obtener criterios filtrados por normas."""
    try:
        if not norms:
            return jsonify({"error": "No norms provided"}), 400

        # Validar que las normas sean válidas
        valid_norms = {'ISO25000', 'IEEE', 'FURPS', 'McCall'}
        invalid_norms = [norm for norm in norms if norm not in valid_norms]
        if invalid_norms:
            return jsonify({"error": f"Invalid norms: {', '.join(invalid_norms)}"}), 400

        criteria = get_criteria_by_norms_db(norms)
        return jsonify(criteria), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving criteria: {str(e)}"}), 500
    
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
    """Servicio para registrar una evaluación."""
    try:
        required_fields = ["id_empresa", "id_usuario", "criterios"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo faltante: {field}"}), 400

        criterios = data["criterios"]
        if not isinstance(criterios, list) or not criterios:
            return jsonify({"error": "Invalido or faltante 'criterios' field"}), 400

        # Registrar la evaluación
        new_evaluation = create_evaluation_db(data)
        if "error" in new_evaluation:
            return jsonify(new_evaluation), 500

        return jsonify({"message": "Evaluacion presentada con exito", "evaluation_id": new_evaluation}), 201
    except Exception as e:
        return jsonify({"error": f"Error al enviar la evaluacion: {str(e)}"}), 500
    
def generate_evaluation_pdf(evaluation_id):
    """Genera un archivo PDF con los detalles de una evaluación."""
    # Obtener los detalles de la evaluación
    evaluation = get_evaluation_details(evaluation_id)
    if not evaluation:
        raise ValueError("Evaluación no encontrada.")
    
    # Crear un objeto PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, txt="Resultados de la Evaluación", ln=True, align="C")
    pdf.ln(10)  # Espacio

    # Detalles
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"ID Evaluación: {evaluation['id_evaluacion']}", ln=True)
    pdf.cell(200, 10, txt=f"Empresa: {evaluation['empresa_nombre']}", ln=True)
    pdf.cell(200, 10, txt=f"Usuario: {evaluation['usuario_nombre']}", ln=True)
    pdf.cell(200, 10, txt=f"Fecha de Evaluación: {evaluation['fecha_evaluacion']}", ln=True)
    pdf.cell(200, 10, txt=f"Puntaje Total: {evaluation['puntaje_total']}", ln=True)
    pdf.cell(200, 10, txt=f"Porcentaje Total: {evaluation['porcentaje_total']}%", ln=True)
    pdf.cell(200, 10, txt=f"Resultado: {evaluation['resultado']}", ln=True)

    # Guardar el PDF en un archivo temporal
    file_path = f"evaluacion_{evaluation_id}.pdf"
    pdf.output(file_path)

    return file_path
