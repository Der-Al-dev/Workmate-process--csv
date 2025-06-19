from typing import Dict, List

from .args import Arguments
from .filter import convert
from .operations import AGGREGATE_OP


def is_aggregate(args: Arguments) -> bool:
    result = False
    if args.aggregate:
        result = True
    return result


def apply_aggregation(
    data: List[Dict[str, str]], args: Arguments
) -> List[Dict[str, str]]:
    result = 0.0
    check = 0
    values = process_value(data, args)

    if args.aggregate_op is None:
        raise ValueError("Не указана операция агрегации")

    operation = AGGREGATE_OP.get(args.aggregate_op)

    for op in AGGREGATE_OP:
        if (args.aggregate_op, op) and operation:
            result = operation(values)
            check = 1
            break
    if not check:
        raise ValueError(
            f"Неизвестная операция агрегации: {args.aggregate_op}"
        )

    aggregated_data = [
        {f"{args.aggregate_op}({args.aggregate_column})": str(result)}
    ]

    return aggregated_data


def process_value(data: List[Dict[str, str]], args: Arguments) -> List[float]:
    values = []
    if args.aggregate_column:
        for row in data:
            value_from_db = convert(row[args.aggregate_column])
            values.append(value_from_db)
    return values
