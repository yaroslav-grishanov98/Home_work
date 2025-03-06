import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("account_card, expected", [("Счёт 1234567891234567", "Счёт 1234 56** **** 4567")])
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize("datetime, expected", [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_data(datetime, expected):
    assert get_date(datetime) == expected


@pytest.fixture
def account_card():
    return "Счёт 1234567891234567"


@pytest.fixture
def datetime():
    return "2024-03-11T02:26:18.671407"
