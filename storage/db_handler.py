import psycopg2
from psycopg2.extras import execute_batch
from config import DB_CONFIG
from typing import List, Dict

class DatabaseHandler:
    def __init__(self):
        self.conn = None
        
    def connect(self):
        """Установка соединения с БД"""
        self.conn = psycopg2.connect(**DB_CONFIG)
        
    def disconnect(self):
        """Закрытие соединения"""
        if self.conn:
            self.conn.close()
            
    def save_documents(self, records: List[Dict]):
        """Сохранение документов в БД"""
        if not self.conn:
            self.connect()
            
        query = """
        INSERT INTO documents (
            doc_number, doc_date, amount, 
            supplier, recipient, doc_type
        ) VALUES (%(doc_number)s, %(date)s, %(amount)s, 
                %(supplier)s, %(recipient)s, %(doc_type)s)
        """
        
        with self.conn.cursor() as cursor:
            execute_batch(cursor, query, records)
            self.conn.commit()