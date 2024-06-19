import json
import os


def get_transactions_data(file_path: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях."""

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            transactions_json_data = json.load(f)

            if isinstance(transactions_json_data, list):
                return transactions_json_data

            else:
                return []

    except (json.JSONDecodeError, OSError):
        return []


if __name__ == "__main__":
    file_path = "data\\operations.json"
    transactions = get_transactions_data(file_path)
    print(transactions)
