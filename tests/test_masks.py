from typing import List

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_numbers() -> List[str]:
    """Фикстура, предоставляющая примеры номеров карт для тестирования."""
    return [
        "7000792289606361",
        "1234567890123456",
        "123",
        "",
        "abc"
    ]


@pytest.fixture
def account_numbers() -> List[str]:
    """Фикстура, предоставляющая примеры номеров счетов для тестирования."""
    return [
        "12345678901234567890",
        "7000792289606361",
        "1234",
        "",
        "abcde"
    ]


def test_get_mask_card_number(card_numbers: List[str]) -> None:
    """Тестирование правильности маскирования номера карты."""


    assert get_mask_card_number(card_numbers[0]) == "7000 79** **** 6361"
    assert get_mask_card_number(card_numbers[1]) == "1234 56** **** 3456"
    assert get_mask_card_number(card_numbers[2]) == ""
    assert get_mask_card_number(card_numbers[3]) == ""
    assert get_mask_card_number(card_numbers[4]) == ""


def test_get_mask_account(account_numbers: List[str]) -> None:
    """Тестирование правильности маскирования номера счета."""


    assert get_mask_account(account_numbers[0]) == "**7890"
    assert get_mask_account(account_numbers[1]) == ""
    assert get_mask_account(account_numbers[2]) == ""
    assert get_mask_account(account_numbers[3]) == ""
    assert get_mask_account(account_numbers[4]) == ""



if __name__ == "__main__":
    pytest.main()
