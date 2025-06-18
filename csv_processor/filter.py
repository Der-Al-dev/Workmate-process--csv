from typing import List, Dict, Optional
from .arg_parser import Arguments, FILTER_OP


def is_filter (args: Arguments) -> bool:
    result = False
    if args.where: result = True
    return result


def apply_filter (data: List[Dict[str, str]], args: Arguments)->List[Dict[str, str]]:
    
    value = convert(args.filter_value)
    
    if args.filter_op:
        operation = FILTER_OP.get(args.filter_op)

    data_filtered = []
    if args.filter_column and operation:
        for row in data:
            value_from_db = convert(row[args.filter_column])
            if operation(value_from_db,value):
                data_filtered.append(row)

    return data_filtered


def convert(value: Optional[str]) -> Optional[str | float]:
    result: Optional[str | float] = None
    if value is not None:
        if is_number(value):
            result = float(value)
        else:
            result = value
    return result


def is_number(value: str) -> bool:
    try:
        float(value)
        result = True
    except ValueError: result = False
    return result
        
