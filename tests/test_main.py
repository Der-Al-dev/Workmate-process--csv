import os
import sys

import pytest

import main


def test_main_success(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["program", "-f", "data.csv"])
    monkeypatch.setattr(os.path, "isfile", lambda path: True)
    monkeypatch.setattr(os.path, "isabs", lambda path: True)
    monkeypatch.setattr(main, "load_csv", lambda path: [{"price": "100"}])
    monkeypatch.setattr(main, "is_filter", lambda args: False)
    monkeypatch.setattr(main, "is_aggregate", lambda args: False)
    monkeypatch.setattr(main, "print_table", lambda data: None)
    main.main()


def test_main_with_filter(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["program", "-f", "data.csv"])
    monkeypatch.setattr(os.path, "isfile", lambda path: True)
    monkeypatch.setattr(os.path, "isabs", lambda path: True)
    monkeypatch.setattr(main, "load_csv", lambda path: [{"price": "100"}])
    monkeypatch.setattr(main, "is_filter", lambda args: True)
    monkeypatch.setattr(
        main, "apply_filter", lambda data, args: [{"price": "50"}]
    )
    monkeypatch.setattr(main, "is_aggregate", lambda args: False)
    monkeypatch.setattr(main, "print_table", lambda data: None)
    main.main()


def test_main_with_aggregation(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["program", "-f", "data.csv"])
    monkeypatch.setattr(os.path, "isfile", lambda path: True)
    monkeypatch.setattr(os.path, "isabs", lambda path: True)
    monkeypatch.setattr(main, "load_csv", lambda path: [{"price": "100"}])
    monkeypatch.setattr(main, "is_filter", lambda args: False)
    monkeypatch.setattr(main, "is_aggregate", lambda args: True)
    monkeypatch.setattr(
        main, "apply_aggregation", lambda data, args: [{"sum(price)": 100}]
    )
    monkeypatch.setattr(main, "print_table", lambda data: None)
    main.main()


def test_main_file_not_found(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["program", "-f", "nofile.csv"])
    monkeypatch.setattr(os.path, "isfile", lambda path: False)
    monkeypatch.setattr(os.path, "isabs", lambda path: True)
    with pytest.raises(SystemExit) as excinfo:
        main.main()
    assert excinfo.value.code == 1


def test_main_with_relative_path(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["program", "-f", "data/products.csv"])
    monkeypatch.setattr(os.path, "isfile", lambda path: True)
    monkeypatch.setattr(os.path, "isabs", lambda path: False)
    monkeypatch.setattr(os.path, "dirname", lambda path: "/some/base/dir")
    monkeypatch.setattr(
        os.path, "join", lambda *args: "/some/base/dir/data/products.csv"
    )
    monkeypatch.setattr(main, "load_csv", lambda path: [{"price": "100"}])
    monkeypatch.setattr(main, "is_filter", lambda args: False)
    monkeypatch.setattr(main, "is_aggregate", lambda args: False)
    monkeypatch.setattr(main, "print_table", lambda data: None)
    main.main()
