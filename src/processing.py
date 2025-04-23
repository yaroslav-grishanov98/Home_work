from typing import Any, Dict, Iterable, List


def filter_by_state(transactions: List[Dict], state_word: str) -> List[Dict]:
    """Фильтрует список транзакций по указанному статусу"""
    return [elem for elem in transactions if elem.get("state") == state_word]


def sort_by_date(data: Iterable[Dict[str, Any]], reverse_order: bool = True) -> List[Dict[str, Any]]:
    """Функция сортирует по дате"""

    def data_get(item: Dict[str, Any]) -> Any:
        """Функция вспомагающая, для сортировки"""
        return item["date"]

    return sorted(data, key=data_get, reverse=reverse_order)
