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
    cursor = connection.cursor()
    query = """
        INSERT INTO Usuarios (nombre, correo, contraseña, rol)
        VALUES (%s, %s, %s, %s) RETURNING id_usuario
    """
    cursor.execute(query, (data["nombre"], data["correo"], data["contraseña"], data["rol"]))
    user_id = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return {"id_usuario": user_id, **data}

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
    """Crear una nueva evaluación en la base de datos."""
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO Evaluaciones (id_empresa, id_usuario, puntaje_total, porcentaje_total, resultado)
        VALUES (%s, %s, %s, %s, %s) RETURNING id_evaluacion
    """
    cursor.execute(query, (data["id_empresa"], data["id_usuario"], data["puntaje_total"], data["porcentaje_total"], data["resultado"]))
    evaluation_id = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return {"id_evaluacion": evaluation_id, **data}
