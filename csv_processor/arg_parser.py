import argparse, re
from .args import Arguments
from .operations import FILTER_OP, AGGREGATE_OP

def parse_args() -> Arguments:
    arguments = argparse.ArgumentParser()

    arguments.add_argument(
        '-f','--file',
        dest='file',
        type=str,
        required=True,
        help="Путь к файлу"
    )
    arguments.add_argument(
        '--where',
        dest='where',
        type=str,
        required=False,
        help="Условие фильтрации, например: price<1000, rating=4.5, name=iphone"
    )
    arguments.add_argument(
        '--aggregate',
        dest='aggregate',
        type=str,
        required=False,
        help="Условие агрегации, например: rating=min"
    )

    args = arguments.parse_args(namespace=Arguments())
    if_arg_where(args)
    if_arg_aggregate(args)
    return args


def if_arg_where(args: Arguments) -> None:
    if args.where:
        pattern = r'^([\w\s]+)\s*(' + '|'.join(map(re.escape, FILTER_OP.keys())) + r')\s*(.+)$'
        match = re.match(pattern, args.where)
        if not match:
            raise ValueError(f"Неверный формат фильтрации: {args.where}")
        args.filter_column = match.group(1).strip()
        args.filter_op = match.group(2)
        args.filter_value = match.group(3).strip()
    else:
        args.filter_column = args.filter_op = args.filter_value = None


def if_arg_aggregate(args: Arguments) -> None:
    if args.aggregate:
        pattern = r'^([\w\s]+)\s*=\s*(\w+)$'
        match = re.match(pattern, args.aggregate)
        if not match:
            raise ValueError(f"Неверный формат агрегации: {args.aggregate}")
        
        column = match.group(1).strip()
        operation = match.group(2).strip().lower()

        if operation not in AGGREGATE_OP:
            raise ValueError(f"Неизвестная операция агрегации: {operation}")

        args.aggregate_column = column
        args.aggregate_op = operation
    else:
        args.aggregate_column = args.aggregate_op = None