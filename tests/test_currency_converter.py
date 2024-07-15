import unittest
from unittest.mock import patch, Mock
from external_api.currency_converter import convert_to_rubles


class TestCurrencyConverter(unittest.TestCase):

    @patch('external_api.currency_converter.requests.get')
    def test_convert_to_rubles_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': 75.0}
        mock_get.return_value = mock_response

        result = convert_to_rubles('USD', 1)

        self.assertEqual(result, 75.0)
        mock_get.assert_called_once()

    @patch('external_api.currency_converter.requests.get')
    def test_convert_to_rubles_fail(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = 'Bad Request'
        mock_get.return_value = mock_response

        result = convert_to_rubles('USD', 1)

        self.assertIsNone(result)
        mock_get.assert_called_once()

    def test_convert_to_rubles_same_currency(self):
        result = convert_to_rubles('RUB', 100)

        self.assertEqual(result, 100)


if __name__ == '__main__':
    unittest.main()
