import pytest

from src.filter_transactions import count_transactions_by_categories, filter_transactions_by_description


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
            "description": None,  # проверка на None
            "amount": 100
        }
    ]


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
    """Тест когда нет совпадений"""
    result = filter_transactions_by_description(test_transactions, "несуществующее")
    assert result == []


def test_filter_transactions_by_description_none_description(test_transactions):
    """Тест с None в описании"""
    result = filter_transactions_by_description(test_transactions, "test")
    assert all(transaction.get("description") is not None for transaction in result)


@pytest.fixture
def test_categories():
    """Фикстура с тестовыми категориями"""
    return {
        "Переводы": "перевод",
        "Оплата": "оплата",
        "Другое": "прочее"
    }


def test_count_transactions_by_categories_basic(test_transactions, test_categories):
    """Тест базового подсчета категорий"""
    result = count_transactions_by_categories(test_transactions, test_categories)
    assert result["Переводы"] == 2
    assert result["Оплата"] == 1
    assert result["Другое"] == 0


def test_count_transactions_by_categories_empty_transactions(test_categories):
    """Тест с пустым списком транзакций"""
    result = count_transactions_by_categories([], test_categories)
    assert all(count == 0 for count in result.values())


def test_count_transactions_by_categories_empty_categories(test_transactions):
    """Тест с пустым словарем категорий"""
    result = count_transactions_by_categories(test_transactions, {})
    assert result == {}


def test_count_transactions_by_categories_case_insensitive(test_transactions, test_categories):
    """Тест подсчета без учета регистра"""
    transactions = [
        {"description": "ПЕРЕВОД ОРГАНИЗАЦИИ"},
        {"description": "перевод между счетами"},
    ]
    result = count_transactions_by_categories(transactions, test_categories)
    assert result["Переводы"] == 2


def test_count_transactions_by_categories_none_description(test_transactions, test_categories):
    """Тест с None в описании"""
    transactions = [
        {"description": None},
        {"description": "перевод"},
    ]
    result = count_transactions_by_categories(transactions, test_categories)
    assert result["Переводы"] == 1


def test_count_transactions_by_categories_missing_description(test_categories):
    """Тест с отсутствующим ключом description"""
    transactions = [
        {"amount": 100},
        {"description": "перевод"}
    ]
    result = count_transactions_by_categories(transactions, test_categories)
    assert result["Переводы"] == 1
