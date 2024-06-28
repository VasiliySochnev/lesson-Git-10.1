import csv

file_to_user = "../data/transactions.csv"


def read_from_csv(file_name: str) -> list[dict]:
    """Функция чтения данных из CSV-файла и вывода транзакций в виде списка словарей"""

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader_from_csv = csv.DictReader(file, delimiter=";")
            list_transactions: list = []

            for item in reader_from_csv:
                list_transactions.append(item)

            return list_transactions

    except FileNotFoundError as exp:
        return f"{exp}: Файл не найден"


if __name__ == "__main__":
    print(read_from_csv(file_to_user))
