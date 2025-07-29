import tabula
import pandas as pd
from typing import List, Dict

def parse_pdf(file_path: str) -> List[Dict]:
    """Извлечение данных из PDF"""
    try:
        # Чтение таблиц из PDF
        tables = tabula.read_pdf(
            file_path,
            pages='all',
            multiple_tables=True,
            lattice=True  # Для таблиц с линиями
        )
        
        # Объединение всех таблиц
        combined_df = pd.concat(tables, ignore_index=True)
        
        # Базовая очистка
        combined_df = combined_df.dropna(how='all')
        combined_df = combined_df.map(lambda x: x.strip() if isinstance(x, str) else x)
        
        return combined_df.to_dict('records')
    except Exception as e:
        raise Exception(f"PDF parsing error: {str(e)}")