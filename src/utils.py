import json
import logging
import os

from src.external_api import get_exchange_rate

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(PROJECT_DIR, 'logs', 'example.log')

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(LOG_FILE, mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def load_transactions(file_path):
    """Загружает данные о финансовых транзациях из JSON-файла."""
    logger.info(f"Попытка загрузки транзакций из файла: {file_path}")

    if not os.path.exists(file_path):
        logger.warning(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                logger.info(f"Успешно загружено транзакций: {len(data)}")
                return data
            logger.warning("Загруженные данные не являются списком")
            return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
    except ValueError:
        logger.error(f"Ошибка преобразования данных в файле: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Непредвиденная ошибка при загрузке файла: {e}")
        return []


def convert_transaction_to_rub(transaction):
    """Возвращает сумму в рублях."""
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        logger.info(f"Конвертация транзакции: сумма {amount}, валюта {currency}")

        if currency == "RUB":
            logger.info("Валюта уже в рублях, конвертация не требуется")
            return amount

        if currency not in ["USD", "EUR"]:
            logger.error(f"Неподдерживаемая валюта: {currency}")
            raise ValueError(f"Неподдерживаемая валюта: {currency}")

        exchange_rate = get_exchange_rate(currency)
        if exchange_rate is None:
            logger.error(f"Не удалось получить курс для валюты {currency}")
            raise ValueError(f"Не удалось получить курс для валюты {currency}")

        converted_amount = round(amount * exchange_rate, 2)
        logger.info(
            f"Сконвертировано: {amount} {currency} -> {converted_amount} RUB"
        )
        return converted_amount

    except (KeyError, ValueError) as e:
        logger.error(f"Ошибка при конвертации: {str(e)}")
        raise ValueError(f"Ошибка при конвертации: {str(e)}")


if __name__ == "__main__":
    logger.debug("Тестирование начато")

    test_file = os.path.join(PROJECT_DIR, "operations.json")
    transactions = load_transactions(test_file)
    logger.info(f"Загружено {len(transactions)} транзакций")

    test_transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "USD"
            }
        }
    }
    try:
        rub_amount = convert_transaction_to_rub(test_transaction)
        logger.info(f"Тестовая конвертация: {rub_amount} RUB")
    except ValueError as e:
        logger.error(f"Ошибка при тестовой конвертации: {e}")

    logger.debug("Тестирование завершено")
