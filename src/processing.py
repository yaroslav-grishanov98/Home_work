from typing import Any, Iterable


def filter_by_state(list_dictionary: list[dict], state_word: str = "EXECUTED") -> list[dict]:
    """Функция перебирает список словарей по ключу"""

    dict_state = []
    for elem in list_dictionary:
        if elem["state"] == state_word:
            dict_state.append(elem)
    return dict_state


def sort_by_date(data: Iterable[dict], reverse_order=True) -> list[dict]:
    """Функция сортирует по дате"""

    def data_get(item: dict) -> Any:
        """Функция вспомогающая, для сортировки"""
        return item["date"]

    return sorted(data, key=data_get, reverse=reverse_order)