import logging

import os

# Получаем путь к директории src
SRC_DIR = os.path.dirname(os.path.abspath(__file__))

# Получаем путь к корневой директории проекта (на одну директорию выше src)
BASE_DIR = os.path.dirname(SRC_DIR)

# Создаем путь до директории logs в корне проекта
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Проверяем, существует ли директория logs, если нет - создаем
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Указываем путь до файла с логами
log_file = os.path.join(LOG_DIR, "masks_logger")

# Основная конфигурация logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=log_file,  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске

# Создаем логеры для компонентов программы
masks_card_logger = logging.getLogger("mask.card")
masks_check_logger = logging.getLogger("mask.check")


def mask_card(number_card: str) -> str:
    """Функция, которая возвращает маску номера карты"""

    # Записываем информацию о вводе номера карты
    masks_card_logger.info(f"Getting the card number mask: {number_card}")
    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def mask_check(number_check: str) -> str:
    """Функция, которая возвращает маску счета"""

    # Записываем информацию о вводе номера счета
    masks_check_logger.info(f"Getting an account number mask: {number_check}")
    return f"**{number_check[-4:]}"


if __name__ == "__main__":
    print(mask_card("1111222233335555"))
    print(mask_check("00112233445566778899"))
