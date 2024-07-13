import os

from config import DATA_DIR
from src.processing import new_list_pass_value, sort_date_id_list
from src.read_from_csv import read_from_csv
from src.read_from_excel import read_from_excel
from src.search_transactions import search_transactions
from src.utils import get_transactions_data
from src.widget import date_conversion, mask_type_card_check


def main() -> None:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой."""
    while True:
        print(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла"""
        )
        user_file_choice = input().strip()
        if user_file_choice == "1":
            print("Для обработки выбран JSON-файл.")
            list_transactions = get_transactions_data(os.path.join(DATA_DIR, "operations.json"))
            break
        elif user_file_choice == "2":
            print("Для обработки выбран CSV-файл.")
            list_transactions = read_from_csv(os.path.join(DATA_DIR, "transactions.csv"))
            break
        elif user_file_choice == "3":
            print("Для обработки выбран XLSX-файл.")
            list_transactions = read_from_excel(os.path.join(DATA_DIR, "transactions_excel.xlsx"))
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    filters: dict[str, str | bool] = {}
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"
        ).upper()
        if status in ["CANCELED", "PENDING", "EXECUTED"]:
            filters["status"] = status
            print(f"Операции отфильтрованы по статусу {status}")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue
    while True:
        sort_date = input("Отсортировать операции по дате?  Да/Нет\n").lower()
        if sort_date == "да":
            while True:
                sorting_order = input(
                    """Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n"""
                ).lower()
                if sorting_order == "по возрастанию":
                    filters["date"] = False
                    break
                elif sorting_order == "по убыванию":
                    filters["date"] = True
                    break
                else:
                    print("Некорректный выбор. Попробуйте еще раз.")
                    continue
            break
        elif sort_date == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue
    while True:
        sort_code = str(input("Выводить только рублевые транзакции? Да/Нет\n")).lower()
        if sort_code == "да":
            filters["currency"] = "RUB"
            break
        elif sort_code == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue
    while True:
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет:\n").lower()
        if user_input == "да":
            search = input("Видите слово для поиска: ")
            filters["description"] = search
            break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    transactions = list_transactions
    for filter_type, filter_value in filters.items():
        if filter_type == "status":
            transactions = new_list_pass_value(transactions, filter_value)
        elif filter_type == "date":
            transactions = sort_date_id_list(transactions, filter_value)
        elif filter_type == "currency":
            transactions = [
                txn
                for txn in transactions
                if txn.get("operationAmount", {}).get("currency", {}).get("code") == filter_value
            ]
        elif filter_type == "description":
            transactions = search_transactions(transactions, filter_value)

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}")
    for transaction in transactions:
        description = transaction.get("description")
        if description == "Открытие вклада":
            from_ = description
        else:
            from_ = mask_type_card_check(transaction.get("from"))

        to_ = mask_type_card_check(transaction.get("to"))
        date = date_conversion(transaction.get("date"))

        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]

        if description == "Открытие вклада":
            print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
        else:
            print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
