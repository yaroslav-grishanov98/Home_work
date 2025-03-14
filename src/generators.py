from typing import Dict, Generator, List

"""Функция, принимающая список словарей с транзакциями и возвращающая итератор, 
который поочередно выдает транзакции с заданной валютой."""


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Generator[Dict, None, None]:
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


"""Принимает список словарей с транзакциями и возвращает описание каждой операции."""


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    for transaction in transactions:
        yield transaction.get("description", " ")


"""Выдает номера банковских карт."""


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    for number in range(start, end + 1):
        yield f"{number:04d} {number:04d} {number:04d} {number:04d}"
