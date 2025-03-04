from typing import Any, Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(numbers: Any) -> Any:
    """Mask account or card number based on input type."""
    new_numbers = numbers.split(" ")

    if "Счет" in numbers:
        masked_account = get_mask_account(new_numbers[-1])
        return f"Счет {masked_account}" if masked_account else "Счет "
    else:
        masked_card = get_mask_card_number(new_numbers[-1])
        return masked_card if masked_card else "Карта "


def get_date(date: Union[str]) -> Union[str, int]:
    """Функция, которая возвращает дату в формате ДД.ММ.ГГГГ."""

    if not date:  # Проверка на пустую строку
        return ""

    new_data = date.split("T")
    correct_data = new_data[0].split("-")

    return f"{correct_data[2]}.{correct_data[1]}.{correct_data[0]}"
