from typing import List, Dict
from .args import Arguments
from .filter import convert


def is_aggregate (args: Arguments) -> bool:
    result = False
    if args.aggregate: result = True
    return result


def apply_aggregation(data: List[Dict[str, str]], args: Arguments) -> List[Dict[str, str]]:
    result = 0.0
    values = process_value(data, args)

    if args.aggregate_op == 'sum':
        result = sum(values)
    elif args.aggregate_op == 'min':
        result = min(values)
    elif args.aggregate_op == 'max':
        result = max(values)
    elif args.aggregate_op == 'avg':
        result = sum(values)/len(values)
    elif args.aggregate_op == 'count':
        result = len(values)
    else:
        raise ValueError(f"Неизвестная операция агрегации: {args.aggregate_op}")
    aggregated_data = [{f"{args.aggregate_op}({args.aggregate_column})": str(result)}] 

    return aggregated_data


def process_value(data: List[Dict[str, str]], args: Arguments) ->List[float]:
    values = []
    if args.aggregate_column:
        for row in data:
            value_from_db = convert(row[args.aggregate_column])
            values.append(value_from_db)
    return values
