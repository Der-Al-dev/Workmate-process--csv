from csv import DictReader
from typing import List, Dict

def load_csv(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = DictReader(file)
        data = [row for row in reader]
    return data