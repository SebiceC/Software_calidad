from database import get_connection, release_connection

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

# Funciones relacionadas con las matrices de riesgo
def get_all_risk_matrices_db():
    """Obtiene todas las matrices de riesgo de la base de datos."""
    connection = get_connection()
    if connection is None:
        return {"error": "Fallo conexión a la base de datos"}

    try:
        cursor = connection.cursor()
        query = "SELECT * FROM matrices_riesgo"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    except Exception as e:
        connection.close()
        raise Exception(f"Error al obtener matrices de riesgo: {str(e)}")


def create_risk_matrix_db(data):
    """Crea una nueva matriz de riesgo en la base de datos."""
    connection = get_connection()
    if connection is None:
        return {"error": "Fallo conexión a la base de datos"}

    try:
        query = """
            INSERT INTO matrices_riesgo (codigo_riesgo, descripcion, fase, probabilidad, impacto)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor = connection.cursor()
        cursor.execute(query, (data["codigo_riesgo"], data["descripcion"], data["fase"], data["probabilidad"], data["impacto"]))
        connection.commit()
        cursor.close()
        connection.close()
        return data
    except Exception as e:
        connection.close()
        raise Exception(f"Error al crear matriz de riesgo: {str(e)}")


def update_risk_matrix_db(matrix_id, data):
    """Actualiza una matriz de riesgo existente en la base de datos."""
    connection = get_connection()
    if connection is None:
        return {"error": "Fallo conexión a la base de datos"}

    try:
        query = """
            UPDATE matrices_riesgo
            SET codigo_riesgo = %s, descripcion = %s, fase = %s, probabilidad = %s, impacto = %s
            WHERE id = %s
        """
        cursor = connection.cursor()
        cursor.execute(query, (data["codigo_riesgo"], data["descripcion"], data["fase"], data["probabilidad"], data["impacto"], matrix_id))
        connection.commit()
        cursor.close()
        connection.close()
        return data
    except Exception as e:
        connection.close()
        raise Exception(f"Error al actualizar matriz de riesgo: {str(e)}")


def delete_risk_matrix_db(matrix_id):
    """Elimina una matriz de riesgo de la base de datos."""
    connection = get_connection()
    if connection is None:
        return {"error": "Fallo conexión a la base de datos"}

    try:
        query = "DELETE FROM matrices_riesgo WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(query, (matrix_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        connection.close()
        raise Exception(f"Error al eliminar matriz de riesgo: {str(e)}")

def get_risk_matrix_details_db(matrix_id):
    """Obtiene los detalles de una matriz de riesgo según su ID."""
    connection = get_connection()
    if connection is None:
        return {"error": "Fallo conexión a la base de datos"}

    try:
        query = """
            SELECT * 
            FROM matrices_riesgo
            WHERE id = %s
        """
        cursor = connection.cursor()
        cursor.execute(query, (matrix_id,))
        result = cursor.fetchone()  # Usamos fetchone() ya que esperamos solo un resultado
        cursor.close()
        connection.close()
        
        if result is None:
            return {"error": "Matriz de riesgo no encontrada"}
        
        return result
    except Exception as e:
        connection.close()
        raise Exception(f"Error al obtener detalles de la matriz de riesgo: {str(e)}")


# ---- Funciones para Empresas ----

def get_all_companies_db():
    """Obtener todas las empresas desde la base de datos."""
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT id_empresa, nombre, ciudad, email, telefono, nombre_software FROM empresas"
    cursor.execute(query)
    companies = cursor.fetchall()  # Esto devuelve una lista de tuplas
    cursor.close()
    connection.close()

    # Convertir las tuplas a diccionarios
    companies_list = []
    for empresa in companies:
        company_dict = {
            "id_empresa": empresa[0],
            "nombre": empresa[1],
            "ciudad": empresa[2],
            "email": empresa[3],
            "telefono": empresa[4],
            "nombre_software": empresa[5]
        }
        companies_list.append(company_dict)

    return companies_list



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
        
def create_mitigation_matrix(data):
    """Crea una nueva matriz de mitigación vinculada a una matriz de riesgos."""
    connection = get_connection()
    if not connection:
        raise Exception("No se pudo conectar con la base de datos.")
    try:
        with connection.cursor() as cursor:
            # Insertar en MatrizMitigacion
            query_matriz = """
                INSERT INTO MatrizMitigacion (id_empresa, id_usuario, id_matriz_ries)
                VALUES (%s, %s, %s)
                RETURNING id_matriz_mitig;
            """
            cursor.execute(query_matriz, (data["id_empresa"], data["id_usuario"], data["id_matriz_ries"]))
            id_matriz_mitig = cursor.fetchone()[0]

            # Insertar en DetallesMatrizMitigacion
            query_detalle = """
                INSERT INTO DetallesMatrizMitigacion (
                    id_matriz_mitig, codigo_riesgo, amenaza_oportunidad, descripcion_riesgo, 
                    fase, nivel_riesgo, tipo_respuesta, responsable, plan_mitigacion
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            for detalle in data["detalles"]:
                cursor.execute(query_detalle, (
                    id_matriz_mitig,
                    detalle["codigo_riesgo"],
                    detalle["amenaza_oportunidad"],
                    detalle["descripcion_riesgo"],
                    detalle["fase"],
                    detalle["nivel_riesgo"],
                    detalle["tipo_respuesta"],
                    detalle["responsable"],
                    detalle["plan_mitigacion"]
                ))

            connection.commit()
            return id_matriz_mitig
    finally:
        release_connection(connection)
        
def get_mitigation_matrix_by_id(mitigation_id):
    """Obtiene una matriz de mitigación y sus detalles."""
    connection = get_connection()
    if not connection:
        raise Exception("No se pudo conectar con la base de datos.")
    try:
        with connection.cursor() as cursor:
            # Obtener datos principales
            query_matriz = """
                SELECT id_matriz_mitig, id_empresa, id_usuario, id_matriz_ries, fecha_creacion
                FROM MatrizMitigacion
                WHERE id_matriz_mitig = %s;
            """
            cursor.execute(query_matriz, (mitigation_id,))
            matriz = cursor.fetchone()
            if not matriz:
                return None

            # Obtener detalles
            query_detalles = """
                SELECT codigo_riesgo, amenaza_oportunidad, descripcion_riesgo, fase, nivel_riesgo, 
                       tipo_respuesta, responsable, plan_mitigacion
                FROM DetallesMatrizMitigacion
                WHERE id_matriz_mitig = %s;
            """
            cursor.execute(query_detalles, (mitigation_id,))
            detalles = cursor.fetchall()

            return {
                "id_matriz_mitig": matriz[0],
                "id_empresa": matriz[1],
                "id_usuario": matriz[2],
                "id_matriz_ries": matriz[3],
                "fecha_creacion": matriz[4],
                "detalles": [
                    {
                        "codigo_riesgo": d[0],
                        "amenaza_oportunidad": d[1],
                        "descripcion_riesgo": d[2],
                        "fase": d[3],
                        "nivel_riesgo": d[4],
                        "tipo_respuesta": d[5],
                        "responsable": d[6],
                        "plan_mitigacion": d[7]
                    } for d in detalles
                ]
            }
    finally:
        release_connection(connection)
