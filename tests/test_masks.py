import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    """Тестирование правильности маскирования номера карты."""
    card_numbers = ["7000792289606361", "1234567890123456", "123", "", "abc"]

    assert get_mask_card_number(card_numbers[0]) == "7000 79** **** 6361"
    assert get_mask_card_number(card_numbers[1]) == "1234 56** **** 3456"

    with pytest.raises(ValueError):
        get_mask_card_number(card_numbers[2])
    with pytest.raises(ValueError):
        get_mask_card_number(card_numbers[3])
    with pytest.raises(ValueError):
        get_mask_card_number(card_numbers[4])


def test_get_mask_account():
    """Тестирование правильности маскирования номера счета."""
    account_numbers = ["12345678901234567890", "7000792289606361", "1234", "", "abcde"]

    assert get_mask_account(account_numbers[0]) == "**7890"

    with pytest.raises(ValueError):
        get_mask_account(account_numbers[1])
    with pytest.raises(ValueError):
        get_mask_account(account_numbers[2])
    with pytest.raises(ValueError):
        get_mask_account(account_numbers[3])
    with pytest.raises(ValueError):
        get_mask_account(account_numbers[4])
