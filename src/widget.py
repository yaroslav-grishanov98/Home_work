from typing import Any, Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(numbers: str) -> str:
    """Создает маскированное представление номера счета или карты в зависимости от типа."""
    new_numbers = numbers.split(" ")

    if "Счет" in numbers:
        account_number = new_numbers[-1]  # Получаем номер счета
        masked_account = get_mask_account(account_number)
        return f"Счет {masked_account}" if masked_account else "Счет "

    card_number = new_numbers[-1]  # Получаем номер карты
    masked_card = get_mask_card_number(card_number)
    return f"Карта {masked_card}" if masked_card else "Карта "


def get_date(date: Union[str]) -> str:
    """Создает функцию, которая возвращает дату в ДД.ММ.ГГГГ."""

    if not date:  # Проверка на пустую строку
        return ""

    new_data = date.split("T")
    correct_data = new_data[0].split("-")

    if len(correct_data) != 3:  # Проверяем, что есть три части
        raise ValueError('Invalid date format')  # Выбрасываем ошибку, если формат не верный

    return f"{correct_data[2]}.{correct_data[1]}.{correct_data[0]}"