import pytest
from src.widget import mask_account_card, get_date


@pytest.fixture
def account_card_data():
    """Фикстура для тестовых данных карт и счетов."""
    return [
        "Счет 12345678901234567890",  # Правильный номер счета
        "Карта 7000792289606361",       # Правильный номер карты
        "Счет 1234",                    # Неправильный номер счета (менее 20 цифр)
        "Карта 123",                    # Неправильный номер карты (менее 16 цифр)
    ]


@pytest.fixture
def date_data():
    """Фикстура для тестовых данных дат."""
    return [
        "2023-01-01T00:00:00Z",  # Стандартный формат ISO
        "2023-12-31T23:59:59Z",  # Другой стандартный формат
        "2023-02-29T00:00:00Z",  # Год високосный
        "2023-01-01",             # Без времени
        "",                       # Пустая строка
    ]


def test_mask_account_card(account_card_data):
    """Тестирование функции mask_account_card на разных типах данных."""
    assert mask_account_card(account_card_data[0]) == "Счет **7890"  # Применение маски для счета
    assert mask_account_card(account_card_data[1]) == "7000 79** **** 6361"  # Применение маски для карты
    assert mask_account_card(account_card_data[2]) == "Счет "  # Неверный номер счета
    assert mask_account_card(account_card_data[3]) == "Карта "  # Неверный номер карты


def test_get_date(date_data):
    """Тестирование функции get_date на различных форматах даты."""
    assert get_date(date_data[0]) == "01.01.2023"  # Стандартный формат
    assert get_date(date_data[1]) == "31.12.2023"  # Другой стандартный формат
    assert get_date(date_data[2]) == "29.02.2023"  # Високосный год
    assert get_date(date_data[3]) == "01.01.2023"  # Без времени
    assert get_date(date_data[4]) == ""  # Пустая строка


# Запуск тестов:
if __name__ == "__main__":
    pytest.main()