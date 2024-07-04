# Проект для виджета банковских операций клиента
## Этот проект создан для домашнего задания онлайн - университета SkyPro
### Установка:
1. Клонируйте репозиторий:
````shell
git clone https://github.com/VasiliySochnev/lesson-Git-10.1.git
````
2. Установите зависимости:
````
pip install -r requirements.txt
````
---
### Краткое описание:
#### Содержит в себе следующие функции:
1. Функция, которая возвращает маску номера карты. __module masks.py__
    + ***mask_card***
2. Функция, которая возвращает маску счета. __module masks.py__
    + ***mask_check***
3. Функция, которая возвращает исходную строку
    с замаскированным номером карты/счета. __module widget.py__
    + ***mask_type_card_check***
4. Функция, которая конвертирует дату из формата
    гггг.мм.дд в формат дд.мм.гггг  __module widget.py__
    + ***date_conversion***
5. Функция, которая принимает список словарей и значение для ключа
    'state' и возвращает новый список, содержащий только те словари, у которых ключ
    'state' содержит переданное в функцию значение.  __module processing.py__
    + ***new_list_pass_value***
6. Функция, которая принимает список словарей и возвращает список,
    в котором исходные словари отсортированы по убыванию даты (ключ date),
    функция принимает два аргумента, второй задает порядок сортировки (убывание).  __module processing.py__
    + ***sort_date_id_list***
7. Функция, которая принимает коллекцию со списком словарей с банковскими операциями 
   и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.  __module generators.py__
    + ***filter_by_currency***
8. Генератор, который принимает коллекцию со списком словарей с банковскими операциями
    и возвращает описание каждой операции по очереди.  __module generators.py__
    + ***transaction_descriptions***
9. Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX. __module generators.py__
    + ***card_number_generator***
10. Декоратор, который логирует вызов функции и ее результат в файл test_log.txt или в консоль, он принимает 
    один необязательный аргумент filename, который определяет путь к файлу, в который будут записываться логи. 
    Если filename не задан, то логи будут выводиться в консоль. Если вызов функции закончился ошибкой, 
    то записывается сообщение об ошибке и входные параметры функции.  __module decorators.py__
    + ***log***
11. Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    + ***get_transactions_data***
12. Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    + ***get_transaction_amount_in_rubles***
13. Функция чтения данных из CSV - файла и вывода транзакций в виде списка словарей.
    + ***read_from_csv***
14. Функция для чтения Excel - файла и вывода транзакций в виде списка словарей.
    + ***read_from_excel***
---
#### Группы линтеров:
   + ___flake8 = "^7.0.0"___
   + ___mypy = "^1.10.0"___
   + ___black = "^24.4.2"___
   + ___isort = "^5.13.2"___
---
#### Тестовые файлы для функций:
   + ___test_masks.py___
   + ___test_widget.py___
   + ___test_processing.py___
   + ___test_generators.py___
   + ___test_decorators.py___
   + ___test_utils.py___
   + ___test_external_api.py___
   + ___test_read_from_csv.py___
   + ___data/transactions_csv_test.csv___
   + ___test_read_from_excel.py___
---
#### Файл с фикстурами:
   + ___conftest.py___
---
#### Папка с логерами  ***logs***:
   + ___masks_logger.log___
   + ___utils_logger.log___
---
#### Покрытие тестами на данном этапе:
   + ___89%___