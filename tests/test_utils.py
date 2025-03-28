import unittest
from unittest.mock import patch
import json
import tempfile
import os

from src.utils import convert_transaction_to_rub, load_transactions


class TestUtils(unittest.TestCase):
    """Тестирует функции работы с транзакциями."""

    def test_load_transactions_valid_json(self):
        """Тестирует загрузку корректного JSON файла."""
        test_data = [{"test": "data"}]
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tf:
            json.dump(test_data, tf)
            temp_path = tf.name

        try:
            result = load_transactions(temp_path)
            self.assertEqual(result, test_data)
        finally:
            os.unlink(temp_path)

    def test_load_transactions_invalid_json(self):
        """Тестирует загрузку некорректного JSON файла."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tf:
            tf.write("invalid json")
            temp_path = tf.name

        try:
            result = load_transactions(temp_path)
            self.assertEqual(result, [])
        finally:
            os.unlink(temp_path)

    def test_load_transactions_nonexistent_file(self):
        """Тестирует попытку загрузки несуществующего файла."""
        result = load_transactions("nonexistent.json")
        self.assertEqual(result, [])

    @patch('src.utils.get_exchange_rate')
    def test_convert_transaction_to_rub_usd(self, mock_get_exchange_rate):
        """Тестирует конвертацию USD в рубли."""
        # Добавляем случайное значение
        test_rate = 60.0
        mock_get_exchange_rate.return_value = test_rate

        test_amount = 100.00
        transaction = {
            'operationAmount': {
                'amount': str(test_amount),
                'currency': {'code': 'USD'}
            }
        }

        result = convert_transaction_to_rub(transaction)
        expected = round(test_amount * test_rate, 2)

        self.assertEqual(result, expected)
        mock_get_exchange_rate.assert_called_once_with('USD')

    @patch('src.utils.get_exchange_rate')  # Изменен путь для патча
    def test_convert_transaction_to_rub_eur(self, mock_get_exchange_rate):
        """Тестирует конвертацию EUR в рубли."""
        # Добавляем случайное значение
        test_rate = 70.0
        mock_get_exchange_rate.return_value = test_rate

        test_amount = 100.00
        transaction = {
            'operationAmount': {
                'amount': str(test_amount),
                'currency': {'code': 'EUR'}
            }
        }

        result = convert_transaction_to_rub(transaction)
        expected = round(test_amount * test_rate, 2)

        self.assertEqual(result, expected)
        mock_get_exchange_rate.assert_called_once_with('EUR')