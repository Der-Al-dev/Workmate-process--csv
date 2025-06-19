from typing import Dict, List

from .args import Arguments
from .filter import convert
from .operations import SORT_OP


def apply_sorter(
    data: List[Dict[str, str]], args: Arguments
) -> List[Dict[str, str]]:
    sorted_data = data

    if args.order_column and args.order_op:

        def sort_key(row):
            if args.order_column not in row:
                raise ValueError(
                    f"Колонка '{args.order_column}' не найдена в данных."
                )
            return convert(row.get(args.order_column))

        try:
            key_row_pairs = [(sort_key(row), row) for row in data]
            sorted_pairs = SORT_OP[args.order_op](key_row_pairs)
            sorted_data = [row for _, row in sorted_pairs]
        except KeyError:
            raise ValueError(
                f"Неподдерживаемая операция сортировки: {args.order_op}"
            )
        except TypeError:
            raise ValueError(
                f"Не удалось отсортировать по колонке '{args.order_column}'"
                """ — возможно, данные содержат пустые значения"""
                """  или несовместимые типы."""
            )

    return sorted_data
