import unittest
from unittest.mock import patch, mock_open
from utils.file_operations import read_transactions


class TestFileOperations(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='[{"currency": "USD", "amount": 100}]')
    @patch('os.path.exists')
    def test_read_transactions_success(self, mock_exists, mock_open):
        mock_exists.return_value = True

        result = read_transactions('test_file.json')

        self.assertEqual(result, [{"currency": "USD", "amount": 100}])
        mock_open.assert_called_once_with('test_file.json', 'r', encoding='utf-8')

    @patch('builtins.open', new_callable=mock_open, read_data='Invalid JSON')
    @patch('os.path.exists')
    def test_read_transactions_json_error(self, mock_exists, mock_open):
        mock_exists.return_value = True

        result = read_transactions('test_file.json')

        self.assertEqual(result, [])
        mock_open.assert_called_once_with('test_file.json', 'r', encoding='utf-8')

    @patch('os.path.exists')
    def test_read_transactions_file_not_exist(self, mock_exists):
        mock_exists.return_value = False

        result = read_transactions('test_file.json')

        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
