from typing import Any, Iterable


def new_list_pass_value(id_list: list[dict[str, Any]], default_state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, которая принимает список словарей и значение для ключа
    'state' и возвращает новый список, содержащий только те словари, у которых ключ
    'state' содержит переданное в функцию значение"""
    new_id_list = []
    for dict_list_id in id_list:
        if dict_list_id.get("state") == default_state:
            new_id_list.append(dict_list_id)
    return new_id_list


def sort_date_id_list(id_list: Iterable, reverse_list: bool = True) -> Iterable:
    """Функция, которая принимает список словарей и возвращает список,
    в котором исходные словари отсортированы по убыванию даты (ключ date),
    функция принимает два аргумента, второй задает порядок сортировки (убывание)"""
    sort_date_list = sorted(id_list, key=lambda date_dict: date_dict["date"], reverse=reverse_list)
    return sort_date_list
