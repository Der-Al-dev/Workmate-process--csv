from csv_processor.args import Arguments
from csv_processor.filter import apply_filter


def test_apply_filter_gt():
    data = [{"price": "100"}, {"price": "300"}]
    args = Arguments()
    args.filter_column = "price"
    args.filter_op = ">"
    args.filter_value = "150"
    filtered = apply_filter(data, args)
    assert len(filtered) == 1
    assert filtered[0]["price"] == "300"


def test_apply_filter_lt():
    data = [{"price": "100"}, {"price": "300"}, {"price": "1600"}]
    args = Arguments()
    args.filter_column = "price"
    args.filter_op = "<"
    args.filter_value = "1600"
    filtered = apply_filter(data, args)
    assert len(filtered) == 2
    assert filtered[0]["price"] == "100"
    assert filtered[1]["price"] == "300"


def test_apply_filter_eq():
    data = [{"brand": "apple"}, {"brand": "samsung"}, {"brand": "xiaomi"}]
    args = Arguments()
    args.filter_column = "brand"
    args.filter_op = "="
    args.filter_value = "samsung"
    filtered = apply_filter(data, args)
    assert len(filtered) == 1
    assert filtered[0]["brand"] == "samsung"
