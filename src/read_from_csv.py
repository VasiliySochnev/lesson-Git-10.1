import typing

import pandas as pd  # type: ignore


def read_from_csv(path: str) -> list[typing.Dict] | typing.Any:
    """функция принимает путь до csv файла и возвращает список словарей"""
    blank_list: list = []
    transact_list = []
    try:
        df = pd.read_csv(path, delimiter=";", encoding="UTF-8")
        df_list = df.to_dict("records")
        for transaction in df_list:
            transact_list.append(
                {
                    "id": transaction.get("id"),
                    "state": transaction.get("state"),
                    "date": transaction.get("date"),
                    "operationAmount": {
                        "amount": transaction.get("amount"),
                        "currency": {
                            "name": transaction.get("currency_name"),
                            "code": transaction.get("currency_code"),
                        },
                    },
                    "description": transaction.get("description"),
                    "from": transaction.get("from"),
                    "to": transaction.get("to"),
                }
            )
        return transact_list
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found")
        return blank_list


if __name__ == "__main__":
    file_path = "../data/transactions.csv"
    print(read_from_csv(file_path))
