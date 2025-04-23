import pytest

from src.filter_transactions import (
    filter_transactions_by_description,
    count_transactions_by_categories
)


@pytest.fixture
def test_transactions():
    """Фикстура с тестовыми данными транзакций"""
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "amount": 1000
        },
        {
            "id": 2,
            "description": "Оплата услуг",
            "amount": 500
        },
        {
            "id": 3,
            "description": "Перевод между счетами",
            "amount": 2000
        },
        {
            "id": 4,
            "description": None,
            "amount": 100
        }
    ]


@pytest.fixture
def test_categories():
    """Фикстура с тестовыми категориями"""
    return ["Переводы", "Оплата", "Другое"]


def test_filter_transactions_by_description_basic(test_transactions):
    """Тест поиска по описанию"""
    result = filter_transactions_by_description(test_transactions, "Перевод")
    assert len(result) == 2
    assert all("Перевод" in transaction["description"] for transaction in result)


def test_filter_transactions_by_description_case_insensitive(test_transactions):
    """Тест поиска без учета регистра"""
    result = filter_transactions_by_description(test_transactions, "перевод")
    assert len(result) == 2
    assert all("Перевод" in transaction["description"] for transaction in result)


def test_filter_transactions_by_description_empty_search():
    """Тест с пустой строкой поиска"""
    transactions = [{"description": "Test"}]
    result = filter_transactions_by_description(transactions, "")
    assert result == []


def test_filter_transactions_by_description_empty_transactions():
    """Тест с пустым списком транзакций"""
    result = filter_transactions_by_description([], "test")
    assert result == []


def test_filter_transactions_by_description_no_matches(test_transactions):
    """Тест когда нет совпадений."""
    result = filter_transactions_by_description(test_transactions, "несуществующее")
    assert result == []


def test_filter_transactions_by_description_none_description(test_transactions):
    """Тест с None в описании"""
    result = filter_transactions_by_description(test_transactions, "test")
    assert all(transaction.get("description") is not None for transaction in result)


def test_empty_categories():
    transactions = [
        {'description': 'перевод'},
        {'description': 'оплата'},
    ]
    categories = []
    assert count_transactions_by_categories(transactions, categories) == {}

def test_no_matching_transactions():
    transactions = [
        {'description': 'покупка'},
        {'description': 'зарплата'},
    ]
    categories = ['перевод', 'оплата']
    assert count_transactions_by_categories(transactions, categories) == {}

def test_single_matching_transaction():
    transactions = [
        {'description': 'перевод'},
        {'description': 'покупка'},
    ]
    categories = ['перевод']
    assert count_transactions_by_categories(transactions, categories) == {'перевод': 1}

def test_multiple_matching_transactions():
    transactions = [
        {'description': 'перевод'},
        {'description': 'перевод'},
        {'description': 'покупка'},
    ]
    categories = ['перевод']
    assert count_transactions_by_categories(transactions, categories) == {'перевод': 2}

def test_multiple_categories():
    transactions = [
        {'description': 'перевод'},
        {'description': 'оплата'},
        {'description': 'перевод'},
        {'description': 'покупка'},
    ]
    categories = ['перевод', 'оплата']
    assert count_transactions_by_categories(transactions, categories) == {
        'перевод': 2,
        'оплата': 1
    }

def test_transactions_with_none_description():
    transactions = [
        {'description': 'перевод'},
        {'description': None},
        {'description': 'перевод'},
    ]
    categories = ['перевод']
    assert count_transactions_by_categories(transactions, categories) == {'перевод': 2}

def test_case_sensitivity():
    transactions = [
        {'description': 'Перевод'},
        {'description': 'перевод'},
    ]
    categories = ['перевод']
    assert count_transactions_by_categories(transactions, categories) == {'перевод': 1}
