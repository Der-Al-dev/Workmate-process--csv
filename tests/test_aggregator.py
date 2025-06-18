from csv_processor.aggregator import apply_aggregation
from csv_processor.args import Arguments


def test_apply_aggregation_avg():
    data = [{"price": "100"}, {"price": "300"}]
    args = Arguments()
    args.aggregate = "price=avg"
    args.aggregate_column = "price"
    args.aggregate_op = "avg"
    result = apply_aggregation(data, args)
    assert result == [{"avg(price)": "200.0"}]


def test_apply_aggregation_max():
    data = [{"price": "100"}, {"price": "300"}, {"price": "1300"}]
    args = Arguments()
    args.aggregate = "price=max"
    args.aggregate_column = "price"
    args.aggregate_op = "max"
    result = apply_aggregation(data, args)
    assert result == [{"max(price)": "1300.0"}]


def test_apply_aggregation_min():
    data = [{"price": "100"}, {"price": "300"}, {"price": "1300"}]
    args = Arguments()
    args.aggregate = "price=min"
    args.aggregate_column = "price"
    args.aggregate_op = "min"
    result = apply_aggregation(data, args)
    assert result == [{"min(price)": "100.0"}]


def test_apply_aggregation_sum():
    data = [{"price": "100"}, {"price": "300"}, {"price": "1300"}]
    args = Arguments()
    args.aggregate = "price=sum"
    args.aggregate_column = "price"
    args.aggregate_op = "sum"
    result = apply_aggregation(data, args)
    assert result == [{"sum(price)": "1700.0"}]


def test_apply_aggregation_count():
    data = [{"price": "100"}, {"price": "300"}, {"price": "1300"}]
    args = Arguments()
    args.aggregate = "price=count"
    args.aggregate_column = "price"
    args.aggregate_op = "count"
    result = apply_aggregation(data, args)
    assert result == [{"count(price)": "3"}]
