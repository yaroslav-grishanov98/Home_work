import unittest
from unittest.mock import Mock, patch

from src.external_api import get_exchange_rate  # замените your_module на имя вашего модуля


class TestExchangeRate(unittest.TestCase):
    """Тестирует возможные сценарии работы с API для обмена валют."""


    @patch('requests.get')
    @patch('os.getenv')
    def test_get_exchange_rate_success(self, mock_getenv, mock_requests_get):
        """Проверяет успешный ли ответ от API."""


        mock_getenv.return_value = 'fake_api_key'
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'rates': {
                'USD': 0.011
            }
        }
        mock_requests_get.return_value = mock_response

        # Вызов и проверка
        result = get_exchange_rate('USD')
        self.assertEqual(result, 0.011)
        mock_requests_get.assert_called_once_with(
            "http://api.apilayer.com/exchangerates_data/latest?base=RUB&symbols=USD",
            headers={"apikey": "fake_api_key"}
        )

    @patch('requests.get')
    @patch('os.getenv')
    def test_get_exchange_rate_api_error(self, mock_getenv, mock_requests_get):
        """Тестирует правильность обработки неуспешного ответа от сервера."""

        mock_getenv.return_value = 'fake_api_key'
        mock_response = Mock()
        mock_response.status_code = 404
        mock_requests_get.return_value = mock_response

        result = get_exchange_rate('USD')
        self.assertIsNone(result)

    @patch('requests.get')
    @patch('os.getenv')
    def test_get_exchange_rate_invalid_response(self, mock_getenv, mock_requests_get):
        """Проверяет обработку ответа с отсутствующими данными."""

        mock_getenv.return_value = 'fake_api_key'
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'rates': {}
        }
        mock_requests_get.return_value = mock_response

        result = get_exchange_rate('USD')
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
