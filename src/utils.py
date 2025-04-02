import json
import os

from src.external_api import get_exchange_rate


def load_transactions(file_path):
    """Загружает данные о финансовых транзациях из JSON-файла."""

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, ValueError):
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


def convert_transaction_to_rub(transaction):
    """Возвращает сумму в рублях."""
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency == "RUB":
            return amount

        if currency not in ["USD", "EUR"]:
            raise ValueError(f"Неподдерживаемая валюта: {currency}")

        exchange_rate = get_exchange_rate(currency)
        if exchange_rate is None:
            raise ValueError(f"Не удалось получить курс для валюты {currency}")

        return round(amount * exchange_rate, 2)

    except (KeyError, ValueError) as e:
        raise ValueError(f"Ошибка при конвертации: {str(e)}")
