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

