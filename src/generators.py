from typing import Dict, Generator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Generator[Dict, None, None]:
    """Функция, принимающая список словарей с транзакциями и возвращающая итератор,
    который поочередно выдает транзакции с заданной валютой"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции"""
    for transaction in transactions:
        yield transaction.get("description", " ")


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
