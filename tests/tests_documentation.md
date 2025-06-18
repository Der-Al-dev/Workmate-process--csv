# Pytest tests for Workmate-process--csv

## `tests/test_loader.py`
```python
from csv_processor.loader import load_csv
import tempfile
import os

def test_load_csv():
    csv_content = "name,price\nitem1,100\nitem2,200\n"
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as f:
        f.write(csv_content)
        temp_path = f.name

    data = load_csv(temp_path)
    os.unlink(temp_path)

    assert len(data) == 2
    assert data[0]["name"] == "item1"
    assert data[1]["price"] == "200"
```

## `tests/test_filter.py`
```python
from csv_processor.filter import apply_filter
from csv_processor.args import Arguments

def test_apply_filter_gt():
    data = [{"price": "100"}, {"price": "300"}]
    args = Arguments()
    args.filter_column = "price"
    args.filter_op = ">"
    args.filter_value = "150"
    filtered = apply_filter(data, args)
    assert len(filtered) == 1
    assert filtered[0]["price"] == "300"
```

## `tests/test_aggregator.py`
```python
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
```

## `tests/test_parser.py`
```python
import sys
import pytest
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
```
