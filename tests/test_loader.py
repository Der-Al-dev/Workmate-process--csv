import os
import tempfile

from csv_processor.loader import load_csv


def test_load_csv():
    csv_content = "name,price\nitem1,100\nitem2,200\n"
    with tempfile.NamedTemporaryFile(
        mode="w+", delete=False, suffix=".csv"
    ) as f:
        f.write(csv_content)
        temp_path = f.name

    data = load_csv(temp_path)
    os.unlink(temp_path)

    assert len(data) == 2
    assert data[0]["name"] == "item1"
    assert data[1]["price"] == "200"
