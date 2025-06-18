import argparse
from typing import Optional

class Arguments(argparse.Namespace):
    file: str
    where: Optional[str]
    filter_column: Optional[str]
    filter_op: Optional[str]
    filter_value: Optional[str]
    aggregate: Optional[str]
    aggregate_column: Optional[str]
    aggregate_op: Optional[str]