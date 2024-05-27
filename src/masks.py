def mask_card(number_card: str) -> str:
    """Функция, которая возвращает маску номера карты"""

    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def mask_check(number_check: str) -> str:
    """Функция, которая возвращает маску счета"""

    return f"**{number_check[-4:]}"
