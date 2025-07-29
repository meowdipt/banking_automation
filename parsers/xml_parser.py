import xml.etree.ElementTree as ET
from typing import List, Dict

def parse_xml(file_path: str) -> List[Dict]:
    """Извлечение данных из XML"""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        records = []
        for doc in root.findall('document'):
            record = {}
            for child in doc:
                record[child.tag] = child.text
            records.append(record)
            
        return records
    except Exception as e:
        raise Exception(f"XML parsing error: {str(e)}")