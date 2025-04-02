import logging
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(PROJECT_DIR, 'logs', 'example.log')

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(LOG_FILE, mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, маскирует номер карты в формат XXXX XX** **** XXXX."""
    logger.info("Попытка маскирования номера карты")

    try:
        if len(card_number) != 16:
            logger.error(f"Неверная длина номера карты: {len(card_number)}")
            raise ValueError("Неправильный номер карты: должен содержать 16 цифр.")

        masked_number = (
            f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        )
        logger.info("Номер карты успешно замаскирован")
        return masked_number

    except Exception as e:
        logger.error(f"Ошибка при маскировании номера карты: {str(e)}")
        raise


def get_mask_account(mask_account: str) -> str:
    """Функция маскирует номер счета в формат **XXXX."""
    logger.info("Попытка маскирования номера счета")

    try:
        if len(mask_account) < 20:
            logger.error(f"Неверная длина номера счета: {len(mask_account)}")
            raise ValueError(
                "Неправильный номер счета: должен содержать минимум 20 цифр."
            )

        masked_account = f"**{mask_account[-4:]}"
        logger.info("Номер счета успешно замаскирован")
        return masked_account

    except Exception as e:
        logger.error(f"Ошибка при маскировании номера счета: {str(e)}")
        raise


if __name__ == "__main__":
    try:
        card = "1234567890123456"
        masked_card = get_mask_card_number(card)
        logger.debug(f"Тест маскирования карты: {masked_card}")

        account = "12345678901234567890"
        masked_account = get_mask_account(account)
        logger.debug(f"Тест маскирования счета: {masked_account}")

    except Exception as e:
        logger.error(f"Ошибка при тестировании: {str(e)}")
