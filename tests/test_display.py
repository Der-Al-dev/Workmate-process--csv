from csv_processor.display import print_table


def test_print_table_empty(capsys):
    print_table([])
    captured = capsys.readouterr()
    assert "Нет данных для отображения." in captured.out
