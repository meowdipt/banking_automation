import os

# Конфигурация БД
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'banking_docs'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'postgres'),
    'port': os.getenv('DB_PORT', '5432')
}

# Пути к файлам
INPUT_DIR = 'data/input'
PROCESSED_DIR = 'data/processed'
ERROR_DIR = 'data/error'