import os
import shutil
from config import INPUT_DIR, PROCESSED_DIR, ERROR_DIR
from parsers import parse_pdf, parse_excel, parse_xml, parse_edi
from processors.validator import validate_data
from processors.normalizer import normalize_data
from storage.db_handler import DatabaseHandler

def process_documents():
    """Основной процесс обработки документов"""
    # Инициализация БД
    db = DatabaseHandler()
    
    # Создание директорий
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    os.makedirs(ERROR_DIR, exist_ok=True)
    
    # Обработка каждого файла
    for filename in os.listdir(INPUT_DIR):
        file_path = os.path.join(INPUT_DIR, filename)
        
        try:
            # Определение типа файла
            if filename.endswith('.pdf'):
                raw_data = parse_pdf(file_path)
            elif filename.endswith(('.xlsx', '.xls')):
                raw_data = parse_excel(file_path)
            elif filename.endswith('.xml'):
                raw_data = parse_xml(file_path)
            elif filename.endswith('.edi'):
                raw_data = parse_edi(file_path)
            else:
                continue
                
            # Валидация и нормализация
            validated_data = validate_data(raw_data)
            normalized_data = normalize_data(validated_data)
            
            # Сохранение в БД
            if normalized_data:
                db.save_documents(normalized_data)
                
            # Перемещение в обработанные
            shutil.move(file_path, os.path.join(PROCESSED_DIR, filename))
            
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
            shutil.move(file_path, os.path.join(ERROR_DIR, filename))
            
    db.disconnect()

if __name__ == "__main__":
    process_documents()