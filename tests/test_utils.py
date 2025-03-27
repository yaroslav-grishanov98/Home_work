import unittest
from unittest.mock import patch

from src.utils import convert_transaction_to_rub


class TestUtils(unittest.TestCase):

    @patch('src.external_api.get_exchange_rate')
    def test_convert_transaction_to_rub_usd(self, mock_get_exchange_rate):
        """Тестирует конвертацию суммы транзакции из USD в рубли."""
        mock_get_exchange_rate.return_value = 1/75.0

        transaction = {
            'operationAmount': {
                'amount': '100.00',
                'currency': {'code': 'USD'}
            }
        }

        result = convert_transaction_to_rub(transaction)
        self.assertNotEqual(result, 0, "Ошибка конвертации USD: результат не должен быть равен 0")

    @patch('src.external_api.get_exchange_rate')
    def test_convert_transaction_to_rub_eur(self, mock_get_exchange_rate):
        """Тестирует конвертацию суммы транзакции из EUR в рубли."""
        mock_get_exchange_rate.return_value = 1/85.0

        transaction = {
            'operationAmount': {
                'amount': '100.00',
                'currency': {'code': 'EUR'}
            }
        }

        result = convert_transaction_to_rub(transaction)
        self.assertNotEqual(result, 0, "Ошибка конвертации EUR: результат не должен быть равен 0")


if __name__ == '__main__':
    unittest.main()
