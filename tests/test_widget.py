from typing import List

import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def account_card_data() -> List[str]:
    """Фикстура для тестовых данных карт и счетов."""
    return [
        "Счет 12345678901234567890",
        "Карта 7000792289606361",
        "Счет 1234",
        "Карта 123",
    ]

@pytest.fixture
def date_data() -> List[str]:
    """Фикстура для тестовых данных дат."""
    return [
        "2023-01-01T00:00:00Z",
        "2023-12-31T23:59:59Z",
        "2023-02-29T00:00:00Z",
        "2023-01-01",
        "",
    ]

def test_mask_account_card(account_card_data: List[str]) -> None:
    """Тестирование функции mask_account_card на разных типах данных."""
    assert mask_account_card(account_card_data[0]) == "Счет **7890"
    assert mask_account_card(account_card_data[1]) == "7000 79** **** 6361"
    assert mask_account_card(account_card_data[2]) == "Счет "
    assert mask_account_card(account_card_data[3]) == "Карта "

def test_get_date(date_data: List[str]) -> None:
    """Тестирование функции get_date на различных форматах даты."""
    assert get_date(date_data[0]) == "01.01.2023"
    assert get_date(date_data[1]) == "31.12.2023"
    assert get_date(date_data[2]) == "29.02.2023"
    assert get_date(date_data[3]) == "01.01.2023"
    assert get_date(date_data[4]) == ""


if __name__ == "__main__":
    pytest.main()
