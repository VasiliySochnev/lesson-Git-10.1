import pandas as pd

file_to_user_excel = "../data/transactions_excel.xlsx"


def read_from_excel(file_name: str) -> list[dict]:
    """Функция для чтения Excel - файла и вывода транзакций в виде списка словарей."""

    try:
        with open(file_name, "rb") as file:
            from_excel = pd.read_excel(file)
            from_excel_dict = from_excel.to_dict(orient="records")

            return from_excel_dict

    except FileNotFoundError as exp:
        return f"{exp} Файл не найден"


if __name__ == "__main__":
    print(read_from_excel(file_to_user_excel))
