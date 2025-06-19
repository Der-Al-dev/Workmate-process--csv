import sys

from csv_processor.arg_parser import parse_args


def test_parse_args_where(monkeypatch):
    test_args = ["prog", "-f", "file.csv", "--where", "price>100"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = parse_args()
    assert args.filter_column == "price"
    assert args.filter_op == ">"
    assert args.filter_value == "100"


def test_parse_args_aggregate(monkeypatch):
    test_args = ["prog", "-f", "file.csv", "--aggregate", "price=avg"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = parse_args()
    assert args.aggregate_column == "price"
    assert args.aggregate_op == "avg"
