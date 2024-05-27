from src.masks import mask_card, mask_check
from typing import Union


def mask_type_card_check(coming_str: Union[str]) -> Union[str]:
    """Функция, которая возвращает исходную строку с замаскированным номером карты/счета"""

    new_coming_str = coming_str.split()
    mask_number = ""
    for simbol in new_coming_str:
        if simbol.isalpha():
            mask_number += simbol + " "
        elif simbol.isdigit() and len(simbol) == 16:
            mask_number += mask_card(simbol) + " "
        elif simbol.isdigit() and len(simbol) == 20:
            mask_number += mask_check(simbol) + " "
    return mask_number.strip()


def date_conversion(date: str) -> str:
    """Функция, которая конвертирует дату из формата
    гггг.мм.дд в формат дд.мм.гггг"""

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
