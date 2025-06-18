import sys
import os
from csv_processor.loader import load_csv
from csv_processor.display import print_table
from csv_processor.arg_parser import parse_args
from csv_processor.filter import is_filter, apply_filter 
from csv_processor.aggregator import is_aggregate, apply_aggregation

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
    if is_filter(args): data_filtered = apply_filter(data, args)
    else: data_filtered = data
    if not is_aggregate(args): print_table(data_filtered)
    else:
        aggregation_data = apply_aggregation(data_filtered, args)
        print_table(aggregation_data)

        
if __name__ == "__main__":
    main()