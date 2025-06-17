import sys
import os
from csv_processor.loader import load_csv
from csv_processor.display import print_table
from csv_processor.arg_parser import parse_args

def main():
    args = parse_args()

    file_path = args.file
    if not os.path.isabs(file_path):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, file_path)
    if not os.path.isfile(file_path):
        print(f"Ошибка: файл не найден по пути {file_path}", file=sys.stderr)
        sys.exit(1)
        
    data = load_csv(file_path)
    print_table(data)

if __name__ == "__main__":
    main()