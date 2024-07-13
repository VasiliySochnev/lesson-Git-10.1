import typing


def filter_by_currency(
    transactions: typing.List[typing.Dict[str, typing.Any]], currency: str
) -> typing.List[typing.Dict[str, typing.Any]]:
    """Функция, которая принимает коллекцию со списком словарей с банковскими операциями и возвращает итератор,
    который выдает по очереди операции, в которых указана заданная валюта."""

    return (
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("name") == currency
    )


def transaction_descriptions(
    transactions: typing.List[typing.Dict[str, typing.Any]]
) -> typing.Generator[str, None, None]:
    """Генератор, который принимает коллекцию со списком словарей с банковскими операциями
    и возвращает описание каждой операции по очереди."""

    for transaction in transactions:
        yield transaction.get("description", "Описание операции отсутствует")


def card_number_generator(start: int, end: int) -> str:  # type: ignore
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX."""

    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number
