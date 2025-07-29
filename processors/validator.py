from typing import List, Dict

def validate_data(records: List[Dict]) -> List[Dict]:
    """Валидация и очистка данных"""
    validated = []
    required_fields = {'doc_number', 'date', 'amount'}
    
    for record in records:
        # Проверка обязательных полей
        if not required_fields.issubset(record.keys()):
            continue
            
        # Валидация формата даты
        if not validate_date(record.get('date')):
            continue
            
        # Валидация суммы
        try:
            record['amount'] = float(record['amount'])
        except (ValueError, TypeError):
            continue
            
        validated.append(record)
        
    return validated

def validate_date(date_str: str) -> bool:
    """Пример валидации даты"""
    # Реализация проверки формата даты
    return True  # Упрощено