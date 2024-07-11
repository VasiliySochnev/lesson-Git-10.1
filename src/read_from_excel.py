import pandas as pd
from typing import List
import json


def read_from_excel(file_path: str) -> list[dict] | str:
    """Функция для чтения Excel - файла и вывода транзакций в виде списка словарей."""

    try:
        from_excel = pd.read_excel(file_path)
        from_excel_dict = from_excel.to_dict(orient="records")

        return from_excel_dict

    except FileNotFoundError as exp:
        return f"{exp} Файл не найден"


if __name__ == "__main__":
    file_path = "../data/transactions_excel.xlsx"
    print(read_from_excel(file_path))
