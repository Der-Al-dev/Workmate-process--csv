import argparse
from typing import Dict, Optional, Set

from .operations import AGGREGATE_OP, FILTER_OP, SORT_OP


class Arguments(argparse.Namespace):
    file: str
    where: Optional[str]
    filter_column: Optional[str]
    filter_op: Optional[str]
    filter_value: Optional[str]
    aggregate: Optional[str]
    aggregate_column: Optional[str]
    aggregate_op: Optional[str]
    order_by: Optional[str]
    order_column: Optional[str]
    order_op: Optional[str]


class ArgParseConfig:
    def __init__(
        self,
        arg_name: str,
        pattern_template: str,
        operators: Set[str],
        attr_names: Dict[str, Optional[str]],
        error_message: Optional[str] = None,
        ignore_case: bool = True,
    ):
        self.arg_name = arg_name
        self.pattern_template = pattern_template
        self.operators = operators
        self.attr_names = attr_names
        self.error_message = error_message
        self.ignore_case = ignore_case


COMBINED_ARGS_CONFIG = [
    {
        "flags": ["-f", "--file"],
        "dest": "file",
        "required": True,
        "help": "Путь к файлу",
        "parse_config": None,
    },
    {
        "flags": ["-w", "--where"],
        "dest": "where",
        "required": False,
        "help": """Условие фильтрации, например:
        price<1000, rating=4.5, name=iphone""",
        "parse_config": ArgParseConfig(
            arg_name="where",
            pattern_template=r"^([\w\s]+)\s*({operators})\s*(.+)$",
            operators=set(FILTER_OP.keys()),
            attr_names={
                "column": "filter_column",
                "op": "filter_op",
                "value": "filter_value",
            },
            error_message="Неверный формат фильтрации",
        ),
    },
    {
        "flags": ["-a", "--aggregate"],
        "dest": "aggregate",
        "required": False,
        "help": "Условие агрегации, например: rating=min",
        "parse_config": ArgParseConfig(
            arg_name="aggregate",
            pattern_template=r"^([\w\s]+)\s*=\s*({operators})$",
            operators=set(AGGREGATE_OP.keys()),
            attr_names={
                "column": "aggregate_column",
                "op": "aggregate_op",
                "value": None,
            },
            error_message="Неверный формат агрегации",
        ),
    },
    {
        "flags": ["-o", "--order-by"],
        "dest": "order_by",
        "required": False,
        "help": "Сортировка: например price=asc или rating=desc",
        "parse_config": ArgParseConfig(
            arg_name="order_by",
            pattern_template=r"^([\w\s]+)\s*=\s*({operators})$",
            operators=set(SORT_OP.keys()),
            attr_names={
                "column": "order_column",
                "op": "order_op",
                "value": None
            },
            error_message="Неверный формат сортировки",
        ),
    },
]
