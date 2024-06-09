from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions, currency="USD"):
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(1):
        assert (next(usd_transactions)["id"]) == 939719570
        assert (next(usd_transactions)["id"]) == 142264268


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    for expected in expected_descriptions:
        assert next(descriptions) == expected


def test_card_number_generator():
    start = 1
    end = 5
    expected_results = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    generator = card_number_generator(start, end)

    for expected in expected_results:
        assert next(generator) == expected
