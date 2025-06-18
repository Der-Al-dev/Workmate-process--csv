from typing import Dict, Callable, Any

FILTER_OP: Dict[str, Callable[[Any, Any], bool]] = {
    '!=': lambda a, b: a != b,
    '>=': lambda a, b: a >= b,
    '<=': lambda a, b: a <= b,
    '>': lambda a, b: a > b,
    '<': lambda a, b: a < b,
    '=': lambda a, b: a == b
}

AGGREGATE_OP = {
    'min',
    'max',
    'sum',
    'avg',
    'count'
}