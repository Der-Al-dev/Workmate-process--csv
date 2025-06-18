from .aggregator import apply_aggregation, is_aggregate
from .arg_parser import parse_args
from .args import Arguments
from .display import print_table
from .filter import apply_filter, is_filter
from .loader import load_csv
from .operations import AGGREGATE_OP, FILTER_OP

__all__ = [
    "load_csv",
    "print_table",
    "parse_args",
    "FILTER_OP",
    "AGGREGATE_OP",
    "apply_filter",
    "is_filter",
    "apply_aggregation",
    "is_aggregate",
    "Arguments",
]
