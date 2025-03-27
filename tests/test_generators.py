from typing import Dict, Generator, List

import pytest


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Generator[Dict, None, None]:
    """Функция, принимающая список словарей с транзакциями и возвращающая итератор,
    который поочередно выдает транзакции с заданной валютой"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction

@pytest.fixture
def transactions() -> List[Dict]:
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}},
    ]

def test_filter_by_currency(transactions) -> None:
    assert len(list(filter_by_currency(transactions, "USD"))) == 2
    assert len(list(filter_by_currency(transactions, "GBP"))) == 0
    assert len(list(filter_by_currency([], "USD"))) == 0
    assert len(list(filter_by_currency([{"id": 1, "operationAmount": {"currency": {"code": "EUR"}}}], "USD"))) == 0
    assert len(list(filter_by_currency(transactions, "EUR"))) == 1

def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции"""
    for transaction in transactions:
        yield transaction.get("description", "")

@pytest.fixture
def transaction_descriptions_data() -> List[Dict]:
    return [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
    ]

def test_transaction_descriptions(transaction_descriptions_data) -> None:
    descriptions = list(transaction_descriptions(transaction_descriptions_data))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]

    empty_transactions: List[Dict] = []
    result = list(transaction_descriptions(empty_transactions))
    assert result == []

    transactions_with_missing_descriptions = [
        {"description": "Перевод организации"},
        {},
        {"description": "Перевод со счета на счет"},
        {},
    ]
    descriptions_with_missing = list(transaction_descriptions(transactions_with_missing_descriptions))
    assert descriptions_with_missing == [
        "Перевод организации",
        "",
        "Перевод со счета на счет",
        "",
    ]

def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, end + 1):
        yield f"{number:04d} {number:04d} {number:04d} {number:04d}"

def test_card_number_generator() -> None:
    generated_numbers = list(card_number_generator(1, 5))
    expected_numbers = [
        "0001 0001 0001 0001",
        "0002 0002 0002 0002",
        "0003 0003 0003 0003",
        "0004 0004 0004 0004",
        "0005 0005 0005 0005",
    ]
    assert generated_numbers == expected_numbers

    assert list(card_number_generator(1, 1)) == ["0001 0001 0001 0001"]

    boundary_numbers = list(card_number_generator(1, 9999))
    assert len(boundary_numbers) == 9999
    assert all(len(num.replace(" ", "")) == 16 for num in boundary_numbers)

    assert list(card_number_generator(5, 1)) == []
    assert list(card_number_generator(0, 0)) == ["0000 0000 0000 0000"]