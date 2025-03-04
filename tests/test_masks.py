import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_numbers():
    """Фикстура, предоставляющая примеры номеров карт для тестирования."""
    return [
        "7000792289606361",  # Правильный номер карты
        "1234567890123456",  # Корректный номер карты
        "123",  # Неправильный номер (менее 16 цифр)
        "",  # Пустая строка
        "abc"  # Неверный формат
    ]


@pytest.fixture
def account_numbers():
    """Фикстура, предоставляющая примеры номеров счетов для тестирования."""
    return [
        "12345678901234567890",  # Правильный счет
        "7000792289606361",  # Неправильный счет (менее 20 цифр)
        "1234",  # Неправильный счет (меньше 20 символов)
        "",  # Пустая строка
        "abcde"  # Неверный формат
    ]


def test_get_mask_card_number(card_numbers):
    """Тестирование правильности маскирования номера карты."""

    # Проверка правильности маскирования
    assert get_mask_card_number(card_numbers[0]) == "7000 79** **** 6361"
    assert get_mask_card_number(card_numbers[1]) == "1234 56** **** 3456"
    assert get_mask_card_number(card_numbers[2]) == ""  # Менее 16 цифр
    assert get_mask_card_number(card_numbers[3]) == ""  # Пустая строка
    assert get_mask_card_number(card_numbers[4]) == ""  # Неверный формат


def test_get_mask_account(account_numbers):
    """Тестирование правильности маскирования номера счета."""

    # Проверка правильности маскирования
    assert get_mask_account(account_numbers[0]) == "**7890"
    assert get_mask_account(account_numbers[1]) == ""  # Неправильный счет
    assert get_mask_account(account_numbers[2]) == ""  # Менее 20 символов
    assert get_mask_account(account_numbers[3]) == ""  # Пустая строка
    assert get_mask_account(account_numbers[4]) == ""  # Неверный формат


# Запуск тестов:
if __name__ == "__main__":
    pytest.main()