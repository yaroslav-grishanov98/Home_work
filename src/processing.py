from typing import Any, Iterable, List, Dict


def filter_by_state(list_dictionary: List[Dict[str, Any]], state_word: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция перебирает список словарей по ключу"""

    dict_state: List[Dict[str, Any]] = []
    for elem in list_dictionary:
        if elem["state"] == state_word:
            dict_state.append(elem)
    return dict_state


def sort_by_date(data: Iterable[Dict[str, Any]], reverse_order: bool = True) -> List[Dict[str, Any]]:
    """Функция сортирует по дате"""

    def data_get(item: Dict[str, Any]) -> Any:
        """Функция вспомагающая, для сортировки"""
        return item["date"]

    return sorted(data, key=data_get, reverse=reverse_order)
