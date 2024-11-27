from database import get_connection

# ---- Funciones para Usuarios ----

def get_all_users_db():
    """Obtener todos los usuarios desde la base de datos."""
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT id_usuario, nombre, correo, rol FROM Usuarios"
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users


def create_user_db(data):
    """Crear un nuevo usuario en la base de datos."""
    connection = get_connection()
    if connection is None:
        return {"error": "Fallo conexion a la base de datos"}

    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO Usuarios (nombre, correo, contraseña, rol)
            VALUES (%s, %s, %s, %s)
            RETURNING id_usuario, nombre, correo, rol, created_at
        """
        values = (data["nombre"], data["correo"], data["contraseña"], data["rol"])
        cursor.execute(query, values)
        new_user = cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()

        # Convertir el resultado a un diccionario
        return {
            "id_usuario": new_user[0],
            "nombre": new_user[1],
            "correo": new_user[2],
            "rol": new_user[3],
            "created_at": new_user[4]
        }
    except Exception as e:
        return {"error": str(e)}
    

def get_user_by_email_db(correo):
    """Obtener un usuario de la base de datos por su correo."""
    connection = get_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        query = "SELECT id_usuario, nombre, correo, contraseña, rol FROM Usuarios WHERE correo = %s"
        cursor.execute(query, (correo,))
        row = cursor.fetchone()
        cursor.close()
        connection.close()

        if row:
            return {
                "id_usuario": row[0],
                "nombre": row[1],
                "correo": row[2],
                "contraseña": row[3],
                "rol": row[4]
            }
        return None
    except Exception as e:
        return None
    
def get_criteria_by_norms_db(norms):
    """Obtener criterios filtrados por normas y ordenados por porcentaje."""
    connection = get_connection()
    if connection is None:
        return {"error": "Fallo conexion a la base de datos"}

    try:
        cursor = connection.cursor()
        query = """
            SELECT id_criterio, nombre, descripcion, porcentaje, norma
            FROM Criterios
            WHERE norma = ANY(%s)
            ORDER BY porcentaje DESC
        """
        cursor.execute(query, (norms,))
        rows = cursor.fetchall()
        cursor.close()
        connection.close()

        # Convertir los resultados en una lista de diccionarios
        criteria = [
            {
                "id_criterio": row[0],
                "nombre": row[1],
                "descripcion": row[2],
                "porcentaje": row[3],
                "norma": row[4]
            }
            for row in rows
        ]
        return criteria
    except Exception as e:
        return {"error": str(e)}

# ---- Funciones para Empresas ----

def get_all_companies_db():
    """Obtener todas las empresas desde la base de datos."""
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT id_empresa, nombre, direccion, sector FROM Empresas"
    cursor.execute(query)
    companies = cursor.fetchall()
    cursor.close()
    connection.close()
    return companies


def create_company_db(data):
    """Crear una nueva empresa en la base de datos."""
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO Empresas (nombre, direccion, sector)
        VALUES (%s, %s, %s) RETURNING id_empresa
    """
    cursor.execute(query, (data["nombre"], data["direccion"], data["sector"]))
    company_id = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return {"id_empresa": company_id, **data}

# ---- Funciones para Evaluaciones ----

def get_all_evaluations_db():
    """Obtener todas las evaluaciones desde la base de datos."""
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        SELECT id_evaluacion, id_empresa, id_usuario, fecha_evaluacion, puntaje_total, porcentaje_total, resultado
        FROM Evaluaciones
    """
    cursor.execute(query)
    evaluations = cursor.fetchall()
    cursor.close()
    connection.close()
    return evaluations


def create_evaluation_db(data):
    """Registrar una evaluación y sus criterios."""
    connection = get_connection()
    if connection is None:
        return {"error": "Database connection failed"}

    try:
        cursor = connection.cursor()

        # Insertar en Evaluaciones
        query_evaluation = """
            INSERT INTO Evaluaciones (id_empresa, id_usuario)
            VALUES (%s, %s)
            RETURNING id_evaluacion
        """
        cursor.execute(query_evaluation, (data["id_empresa"], data["id_usuario"]))
        evaluation_id = cursor.fetchone()[0]

        # Insertar criterios evaluados
        query_criteria = """
            INSERT INTO DetallesEvaluacion (id_detalle_eva, id_evaluacion, id_criterio, valor, observaciones)
            VALUES (%s, %s, %s, %s)
        """
        for criterio in data["criterios"]:
            cursor.execute(
                query_criteria,
                (
                    evaluation_id,
                    criterio["id_criterio"],
                    criterio["valor"],
                    criterio.get("observaciones", None),
                ),
            )

        connection.commit()
        cursor.close()
        connection.close()
        return evaluation_id
    except Exception as e:
        return {"error": str(e)}
    
def update_user_db(user_id, data):
    """Actualizar un usuario en la base de datos."""
    connection = get_connection()
    if connection is None:
        return {"error": "Fallo conexion a la base de datos"}

    try:
        cursor = connection.cursor()

        # Verificar si el usuario existe
        cursor.execute("SELECT * FROM Usuarios WHERE id_usuario = %s", (user_id,))
        user = cursor.fetchone()

        if not user:
            return None  # Usuario no encontrado

        # Construir la consulta de actualización
        query = """
            UPDATE Usuarios
            SET nombre = %s, correo = %s, contraseña = %s, rol = %s
            WHERE id_usuario = %s
            RETURNING id_usuario, nombre, correo, rol, created_at
        """
        values = (data["nombre"], data["correo"], data["contraseña"], data["rol"], user_id)
        cursor.execute(query, values)
        updated_user = cursor.fetchone()

        connection.commit()
        cursor.close()
        connection.close()

        return {
            "id_usuario": updated_user[0],
            "nombre": updated_user[1],
            "correo": updated_user[2],
            "rol": updated_user[3],
            "created_at": updated_user[4]
        }
    except Exception as e:
        return {"error": str(e)}

def delete_user_db(user_id):
    """Eliminar un usuario de la base de datos."""
    connection = get_connection()
    if connection is None:
        return {"error": "Fallo conexion a la base de datos"}

    try:
        cursor = connection.cursor()

        # Verificar si el usuario existe
        cursor.execute("SELECT * FROM Usuarios WHERE id_usuario = %s", (user_id,))
        user = cursor.fetchone()

        if not user:
            return None  # Usuario no encontrado

        # Eliminar el usuario
        cursor.execute("DELETE FROM Usuarios WHERE id_usuario = %s", (user_id,))
        connection.commit()

        cursor.close()
        connection.close()

        return True  # Usuario eliminado con éxito
    except Exception as e:
        return {"error": str(e)}

