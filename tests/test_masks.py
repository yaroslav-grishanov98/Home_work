import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    """Тестирование правильности маскирования номера карты."""

    # Проверка правильности маскирования
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"

    # Граничные случаи и нестандартные длины
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number("123") == ""  # Менее 16 цифр
    assert get_mask_card_number("") == ""  # Пустая строка

    # Проверка обработки строки без номера карты
    assert get_mask_card_number("abc") == ""


def test_get_mask_account():
    """Тестирование правильности маскирования номера счета."""

    # Проверка правильности маскирования
    assert get_mask_account("12345678901234567890") == "**7890"
    assert get_mask_account("7000792289606361") == ""

    # Проверка работы с различными форматами и длинами
    assert get_mask_account("12345678901234567890") == "**7890"
    assert get_mask_account("1234") == ""  # Менее 20 символов
    assert get_mask_account("") == ""  # Пустая строка

    # Проверка обработки строки без номера счета
    assert get_mask_account("abcde") == ""


# Запуск тестов:
if __name__ == "__main__":
    pytest.main()