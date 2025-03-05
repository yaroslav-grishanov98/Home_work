import pytest
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("account_card, expected", [
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Карта 4000000000000000", "Карта 4000 00** **** 0000"),
    ("Счет 1234", "Счет "),
    ("Карта 1234567890123456", "Карта 1234 56** **** 3456"),
])
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("", ""),
    ("2024-03-11", "11.03.2024"),
    ("2024-03-11T00:00:00Z", "11.03.2024"),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected

if __name__ == "__main__":
    pytest.main()
