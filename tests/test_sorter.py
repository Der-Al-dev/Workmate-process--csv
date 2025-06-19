import pytest

from csv_processor.args import Arguments
from csv_processor.sorter import apply_sorter


def test_apply_sorter_asc():
    data = [{"price": "300"}, {"price": "100"}, {"price": "200"}]
    args = Arguments()
    args.order_column = "price"
    args.order_op = "asc"
    sorted_data = apply_sorter(data, args)
    prices = [row["price"] for row in sorted_data]
    assert prices == ["100", "200", "300"]


def test_apply_sorter_desc():
    data = [{"price": "300"}, {"price": "100"}, {"price": "200"}]
    args = Arguments()
    args.order_column = "price"
    args.order_op = "desc"
    sorted_data = apply_sorter(data, args)
    prices = [row["price"] for row in sorted_data]
    assert prices == ["300", "200", "100"]


def test_apply_sorter_invalid_column():
    data = [{"price": "300"}, {"price": "100"}]
    args = Arguments()
    args.order_column = "not_a_column"
    args.order_op = "asc"
    with pytest.raises(
        ValueError, match="Колонка 'not_a_column' не найдена в данных."
    ):
        apply_sorter(data, args)
