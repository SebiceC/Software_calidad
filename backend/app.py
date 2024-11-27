from flask import Flask, jsonify, request
from flask_cors import CORS
from model import get_all_users_db, create_user_db, get_user_by_email_db
import psycopg2


app = Flask(__name__)
CORS(app)



@app.route('/usuarios', methods=['POST'])
def create_usuario():
    """Endpoint para crear un nuevo usuario."""
    data = request.get_json()  # Obtener los datos del cuerpo de la solicitud
    new_user = create_user_db(data)  # Llamar a la función para crear el usuario
    if 'error' in new_user:
        return jsonify(new_user), 400  # Enviar error si ocurre algo
    return jsonify(new_user), 201  # Si todo es exitoso, retornar el nuevo usuario creado


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Validar si se recibieron ambos parámetros
    if not email or not password:
        return jsonify({"error": "Correo y contraseña son requeridos"}), 400

    # Obtener el usuario de la base de datos
    user = get_user_by_email_db(email)

    if user is None:
        return jsonify({"error": "Correo o contraseña incorrectos"}), 401

    # Comparar la contraseña ingresada con la almacenada en la base de datos (sin hash)
    if password != user["contraseña"]:
        return jsonify({"error": "Correo o contraseña incorrectos"}), 401

    # Si la contraseña es correcta, puedes devolver un mensaje de éxito
    return jsonify({
        "message": "Inicio de sesión exitoso",
        "user": {
            "id_usuario": user["id_usuario"],
            "nombre": user["nombre"],
            "correo": user["correo"],
            "rol": user["rol"]
        }
    }), 200

@app.route('/register_company', methods=['POST'])
def register_company():
    data = request.get_json()  # Recibe los datos del formulario como JSON
    
    # Obtener los campos del formulario
    nombre = data.get('nombre')
    ciudad = data.get('ciudad')
    email = data.get('email')
    telefono = data.get('telefono')
    nombre_software = data.get('nombre_software')

    # Validar que los campos no estén vacíos
    if not nombre or not ciudad or not email or not telefono or not nombre_software:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    # Conexión a la base de datos
    try:
        connection = psycopg2.connect(
            host="localhost",  # Cambiar por tu configuración de conexión
            database="calidad",  # Nombre de la base de datos
            user="usuario",  # Tu usuario de base de datos
            password="contraseña"  # Tu contraseña de base de datos
        )
        cursor = connection.cursor()
        
        # Consulta SQL para insertar una nueva empresa
        query = """
        INSERT INTO empresas (nombre, ciudad, email, telefono, nombre_software)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nombre, ciudad, email, telefono, nombre_software))
        
        # Confirmar los cambios
        connection.commit()
        
        cursor.close()
        connection.close()

        return jsonify({"message": "Empresa registrada exitosamente"}), 201
    except Exception as e:
        print(f"Error al registrar la empresa: {e}")
        return jsonify({"error": "Hubo un problema al registrar la empresa"}), 500



if __name__ == '__main__':
    app.run(debug=True)
