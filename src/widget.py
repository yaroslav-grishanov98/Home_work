from typing import Any, Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(numbers: Any) -> Any:
    """Создаем новую функцию, которая также макскирует номер, но теперь с названием счета (карты)"""
    new_numbers = numbers.split(" ")
    if "Счет" in numbers:
        return f"Счет {get_mask_account(numbers)}"
    else:
        return f"{' '.join(new_numbers[0:-1])} {get_mask_card_number(new_numbers[-1])}"


def get_date(date: Union[str]) -> Union[str, int]:
    """Создаем функцию, которая возвращает дату в ДД.ММ.ГГГГ"""

    new_data = date.split("T")
    correct_data = new_data[0].split("-")

    return f"{correct_data[2]}.{correct_data[1]}.{correct_data[0]}"
