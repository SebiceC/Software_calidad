from database import get_connection

def fetch_users():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
    finally:
        connection.close()