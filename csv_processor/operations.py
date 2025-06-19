from typing import Any, Callable, Dict, List, Union

FILTER_OP: Dict[str, Callable[[Any, Any], bool]] = {
    "!=": lambda a, b: a != b,
    ">=": lambda a, b: a >= b,
    "<=": lambda a, b: a <= b,
    ">": lambda a, b: a > b,
    "<": lambda a, b: a < b,
    "=": lambda a, b: a == b,
}


AGGREGATE_OP: Dict[str, Callable[[List[float]], Union[float, int]]] = {
    "min": lambda values: min(values) if values else 0,
    "max": lambda values: max(values) if values else 0,
    "avg": lambda values: sum(values) / len(values) if values else 0,
    "sum": lambda values: sum(values),
    "count": lambda values: len(values),
}


SORT_OP: Dict[str, Callable[[List[Any]], List[Any]]] = {
    "asc": lambda items: sorted(items, key=lambda x: x[0]),
    "desc": lambda items: sorted(items, key=lambda x: x[0], reverse=True),
}
