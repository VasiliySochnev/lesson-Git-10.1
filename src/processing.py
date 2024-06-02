from typing import Iterable


def new_list_pass_value(id_list: Iterable, default_state: str = "EXECUTED") -> Iterable:
    """Функция, которая принимает список словарей и значение для ключа
    'state' и возвращает новый список, содержащий только те словари, у которых ключ
    'state' содержит переданное в функцию значение"""
    new_id_list = []
    for dict_list in id_list:
        if dict_list["state"] == default_state:
            new_id_list.append(dict_list)
    return new_id_list


def sort_date_id_list(id_list: Iterable, reverse_list: bool = True) -> Iterable:
    """Функция, которая принимает список словарей и возвращает список,
    в котором исходные словари отсортированы по убыванию даты (ключ date),
    функция принимает два аргумента, второй задает порядок сортировки (убывание)"""
    sort_date_list = sorted(id_list, key=lambda date_dick: date_dick["date"], reverse=reverse_list)
    return sort_date_list
