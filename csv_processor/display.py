from typing import List, Dict
from tabulate import tabulate

def print_table(data: List[Dict[str, str]]) -> None:
    if not data:
        print("Нет данных для отображения.")
        return
    print(tabulate(data, headers="keys", tablefmt="grid"))
