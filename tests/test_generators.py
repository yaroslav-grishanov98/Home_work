from typing import Dict, Generator, List

import pytest


# Функция для фильтрации по валюте
def filter_by_currency(transactions: List[Dict], currency_code: str) -> Generator[Dict, None, None]:
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


# Тесты для функции фильтрации валюты
def test_filter_by_currency(transactions) -> None:
    assert len(list(filter_by_currency(transactions, "USD"))) == 2
    assert len(list(filter_by_currency(transactions, "GBP"))) == 0
    assert len(list(filter_by_currency([], "USD"))) == 0
    assert len(list(filter_by_currency([{"id": 1, "operationAmount": {"currency": {"code": "EUR"}}}], "USD"))) == 0

    # Тест на случаи, когда транзакции отсутствуют
    assert len(list(filter_by_currency(transactions, "EUR"))) == 1


# Функция для получения описаний транзакций
def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    for transaction in transactions:
        yield transaction.get("description", "")


@pytest.fixture
def transaction_descriptions_data() -> List[Dict]:
    return [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
    ]


# Тесты для функции транзакций
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


# Генератор для номеров карт
def card_number_generator(start: int, end: int):
    for number in range(start, end + 1):
        yield f"{number:04d} {number:04d} {number:04d} {number:04d}"


# Тесты для генератора номеров карт
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

    # Тест на случаи с пустым диапазоном
    assert list(card_number_generator(5, 1)) == []  # Пустой диапазон

    # Проверка крайних значений
    assert list(card_number_generator(0, 0)) == ["0000 0000 0000 0000"]
