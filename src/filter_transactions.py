import re
from collections import Counter
from typing import Dict, List


def filter_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """Функция фильтрует транзакции по наличию строки поиска в описании"""

    if not transactions or not search_string:
        return []

    pattern = re.compile(search_string, re.IGNORECASE)
    filtered_transactions = [
        transaction for transaction in transactions
        if 'description' in transaction
           and transaction['description'] is not None
           and pattern.search(transaction['description'])
    ]

    return filtered_transactions


def count_transactions_by_categories(
        transactions: List[Dict],
        categories_dict: Dict[str, str]
) -> Dict[str, int]:
    """Подсчитывает количество операций для каждой категории"""

    counter = Counter({category: 0 for category in categories_dict})

    for transaction in transactions:
        if 'description' not in transaction or transaction['description'] is None:
            continue

        description = transaction['description'].lower()

        for category_key, category_pattern in categories_dict.items():
            if category_pattern.lower() in description:
                counter[category_key] += 1

    return dict(counter)
