import functools


def log(filename=None):
    """Декоратор, который логирует вызов функции и ее результат в файл или в консоль,
    он принимает один необязательный аргумент filename, который определяет путь к файлу,
    в который будут записываться логи. Если filename не задан, то логи будут выводиться в консоль.
    Если вызов функции закончился ошибкой, то записывается сообщение об ошибке и входные параметры функции."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(message + "\n")
                else:
                    print(message)
                raise

        return wrapper

    return decorator
