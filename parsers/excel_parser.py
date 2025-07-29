import pandas as pd
from typing import List, Dict

def parse_excel(file_path: str) -> List[Dict]:
    """Извлечение данных из Excel"""
    try:
        # Автоопределение формата
        df = pd.read_excel(file_path, engine='openpyxl')
        
        # Очистка данных
        df = df.dropna(how='all')
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
        
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f"Excel parsing error: {str(e)}")