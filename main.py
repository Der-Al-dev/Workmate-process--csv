import sys
import os
from csv_processor.loader import load_csv
from csv_processor.display import print_table

def main():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, 'data', 'products.csv')
    data = load_csv(file_path)
    print_table(data)

if __name__ == "__main__":
    main()