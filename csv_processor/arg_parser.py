import argparse

def parse_args() -> argparse.Namespace:
    arguments = argparse.ArgumentParser()
    arguments.add_argument(
        '-f','--file',
        dest='file',
        type=str,
        required=True,
        help="нужно указать путь к файлу"
    )
    args = arguments.parse_args()
    return args