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
    # Conexión a la base de datos
    connection = get_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para insertar una nueva empresa
    query = """
        INSERT INTO Empresas (nombre, ciudad, email, telefono, nombre_software)
        VALUES (%s, %s, %s, %s, %s) RETURNING id_empresa
    """
    
    # Ejecutar la consulta con los datos proporcionados
    cursor.execute(query, (data["nombre"], data["ciudad"], data["email"], data["telefono"], data["nombre_software"]))
    
    # Obtener el id de la empresa recién insertada
    company_id = cursor.fetchone()[0]
    
    # Confirmar los cambios en la base de datos
    connection.commit()
    
    # Cerrar la conexión y el cursor
    cursor.close()
    connection.close()
    
    # Retornar los datos con el id de la empresa
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

def get_evaluation_details(evaluation_id):
    """Obtiene los detalles de una evaluación por su ID."""
    connection = get_connection()
    if not connection:
        raise Exception("No se pudo conectar con la base de datos.")
    try:
        with connection.cursor() as cursor:
            query = """
                SELECT 
                    e.id_evaluacion, e.fecha_evaluacion, e.puntaje_total, e.porcentaje_total, e.resultado,
                    emp.nombre AS empresa_nombre, u.nombre AS usuario_nombre
                FROM Evaluaciones e
                JOIN Empresas emp ON e.id_empresa = emp.id_empresa
                JOIN Usuarios u ON e.id_usuario = u.id_usuario
                WHERE e.id_evaluacion = %s;
            """
            cursor.execute(query, (evaluation_id,))
            evaluation = cursor.fetchone()
            if evaluation:
                return {
                    "id_evaluacion": evaluation[0],
                    "fecha_evaluacion": evaluation[1],
                    "puntaje_total": evaluation[2],
                    "porcentaje_total": evaluation[3],
                    "resultado": evaluation[4],
                    "empresa_nombre": evaluation[5],
                    "usuario_nombre": evaluation[6],
                }
            else:
                return None
    finally:
        release_connection(connection)
