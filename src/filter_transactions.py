import re
from collections import Counter
from typing import Dict, List


def filter_transactions_by_description(
    transactions: List[Dict],
    search_string: str
) -> List[Dict]:
    """Фильтрует транзакции по наличию строки поиска в описании"""
    if not transactions or not search_string:
        return []

    pattern = re.compile(search_string, re.IGNORECASE)

    return [
        transaction for transaction in transactions
        if transaction.get('description') and
        pattern.search(transaction['description'])
    ]


def count_transactions_by_categories(
    transactions: List[Dict],
    categories: List[str]
) -> Dict[str, int]:
    """Подсчитывает количество операций для каждой категории"""
    if not categories:
        return {}

    counter = Counter({category: 0 for category in categories})

    category_mapping = {
        'Переводы': ['перевод'],
        'Оплата': ['оплата'],
        'Другое': ['прочее']
    }

    for transaction in transactions:
        description = transaction.get('description')
        if description is None:
            continue

        description = description.lower()

        for category, patterns in category_mapping.items():
            if any(pattern in description for pattern in patterns):
                counter[category] += 1

    return dict(counter)
