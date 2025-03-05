import pytest
from src.widget import get_date, mask_account_card

# Параметризованные тесты для функции mask_account_card
@pytest.mark.parametrize("account_card, expected", [
    ("Счет 12345678901234567890", "Счет **7890"),  # Ожидаем маскированный номер счета
    ("Карта 4000000000000000", "Карта 4000 00** **** 0000"),  # Ожидаем маскированный номер карты
    ("Счет 1234", "Счет "),  # Неполный номер счета
    ("Карта 1234567890123456", "Карта 1234 56** **** 3456"),  # Ожидаем маскированный номер карты
])
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected

# Параметризованные тесты для функции get_date
@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),  # Ожидаем правильный формат даты
    ("", ""),  # Проверяем пустую строку
    ("2024-03-11", "11.03.2024"),  # Проверяем формат без времени
    ("2024-03-11T00:00:00Z", "11.03.2024"),  # Проверяем ISO формат
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected

if __name__ == "__main__":
    pytest.main()
