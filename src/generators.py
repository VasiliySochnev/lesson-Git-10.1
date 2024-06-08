from typing import List, Dict, Any, Generator


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) ->List[Dict[str, Any]]:
    return (transaction for transaction in transactions
            if transaction.get('operationAmount', {}).get('currency', {}).get('name') == currency)


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    transaction_list = transactions[0]
    for transaction in transaction_list:
        yield transaction.get("description", "Описание операции отсутствует")



