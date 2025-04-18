from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.transactions_reader import _convert_value, read_csv_transactions, read_excel_transactions

CSV_TEST_DATA = """Category,Amount,Date
Groceries,50.5,2023-01-15
Salary,2000.0,2023-01-31
"""

EXCEL_TEST_DATA = {
    'Category': ['Rent', 'Utilities'],
    'Amount': [1000.0, 150.5],
    'Date': ['2023-02-01', '2023-02-15']
}


def test_read_csv_transactions():
    """Тест читающий CSV при помощи мок"""
    mock_file = mock_open(read_data=CSV_TEST_DATA)

    with patch('builtins.open', mock_file):
        with patch('csv.DictReader') as mock_csv_reader:
            mock_csv_reader.return_value = [
                {
                    'Category': 'Groceries',
                    'Amount': '50.5',
                    'Date': '2023-01-15'
                },
                {
                    'Category': 'Salary',
                    'Amount': '2000.0',
                    'Date': '2023-01-31'
                }
            ]

            transactions = read_csv_transactions('fake_path.csv')
            assert len(transactions) == 2
            assert transactions[0]['Amount'] == 50.5
            assert transactions[1]['Amount'] == 2000.0


def test_read_excel_transactions():
    """Тест читающий excel с помощью мок"""
    test_dataframe = pd.DataFrame(EXCEL_TEST_DATA)

    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.return_value = test_dataframe

        transactions = read_excel_transactions('fake_path.xlsx')
        assert len(transactions) == 2
        assert transactions[0]['Amount'] == 1000.0
        assert transactions[1]['Amount'] == 150.5


def test_read_csv_file_not_found():
    """Тест выдаюший ошибку если CSV не найдет"""
    with patch('builtins.open', side_effect=FileNotFoundError):
        transactions = read_csv_transactions('non_existent.csv')
        assert transactions == []


def test_read_excel_file_not_found():
    """Тест выдающий ошибку если excel не найден"""
    with patch('pandas.read_excel', side_effect=FileNotFoundError):
        transactions = read_excel_transactions('non_existent.xlsx')
        assert transactions == []


def test_convert_value():
    """Тест для преобразования значений"""
    test_cases = [
        ('50.5', 50.5),
        ('50,5', 50.5),
        ('  100  ', 100.0),
        ('abc', 'abc'),
        (42, 42)
    ]

    for input_value, expected_value in test_cases:
        result = _convert_value(input_value)
        assert result == expected_value
