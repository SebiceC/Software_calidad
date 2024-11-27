from flask import Flask, jsonify, request
from flask_cors import CORS
from model import get_all_users_db, create_user_db, get_user_by_email_db

app = Flask(__name__)
CORS(app)

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    """Endpoint para obtener todos los usuarios."""
    users = get_all_users_db()
    return jsonify(users)

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    """Endpoint para crear un nuevo usuario."""
    data = request.get_json()  # Obtener los datos del cuerpo de la solicitud
    new_user = create_user_db(data)  # Llamar a la función para crear el usuario
    if 'error' in new_user:
        return jsonify(new_user), 400  # Enviar error si ocurre algo
    return jsonify(new_user), 201  # Si todo es exitoso, retornar el nuevo usuario creado


@app.route('/usuarios/<email>', methods=['GET'])
def get_usuario_por_email(email):
    """Endpoint para obtener un usuario por su correo."""
    user = get_user_by_email_db(email)
    if user:
        return jsonify(user)
    return jsonify({"error": "Usuario no encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)
