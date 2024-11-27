# config.py
from dotenv import load_dotenv
import os

# Cargar el archivo .env
load_dotenv()

# Ahora puedes acceder a las variables de entorno
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'calidad')
DB_USER = os.getenv('DB_USER', 'admin')
DB_PASSWORD = os.getenv('DB_PASSWORD', '123456')
DB_PORT = os.getenv('DB_PORT', 5432)
