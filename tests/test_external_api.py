import unittest
from unittest.mock import Mock, patch

from src.external_api import get_exchange_rate


class TestExchangeRate(unittest.TestCase):
    """Тестирует возможные сценарии работы с API для обмена валют."""

    @patch('requests.get')
    @patch('os.getenv')
    def test_get_exchange_rate_success(self, mock_getenv, mock_requests_get):
        """Проверяет успешный ответ от API."""

        mock_getenv.return_value = 'fake_api_key'
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'result': 75.0
        }
        mock_requests_get.return_value = mock_response


        result = get_exchange_rate('USD')


        self.assertEqual(result, 75.0)


        mock_requests_get.assert_called_once()
        call_args = mock_requests_get.call_args
        self.assertEqual(call_args[1]['headers'], {'apikey': 'fake_api_key'})
        self.assertEqual(call_args[1]['params'], {
            'from': 'USD',
            'to': 'RUB',
            'amount': 1
        })

    @patch('requests.get')
    @patch('os.getenv')
    def test_get_exchange_rate_api_error(self, mock_getenv, mock_requests_get):
        """Проверяет обработку ошибки API."""
        mock_getenv.return_value = 'fake_api_key'
        mock_response = Mock()
        mock_response.status_code = 400
        mock_requests_get.return_value = mock_response

        result = get_exchange_rate('USD')
        self.assertIsNone(result)

    @patch('requests.get')
    @patch('os.getenv')
    def test_get_exchange_rate_missing_result(self, mock_getenv, mock_requests_get):
        """Проверяет обработку ответа без нужных данных."""
        mock_getenv.return_value = 'fake_api_key'
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_requests_get.return_value = mock_response

        result = get_exchange_rate('USD')
        self.assertIsNone(result)


