import csv
from typing import Dict, List

import pandas as pd


def read_csv_transactions(file_path: str = 'data/transactions.csv') -> List[Dict]:
    """Чтение файла CSV"""
    try:
        transactions = []
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                transactions.append({
                    key: _convert_value(value) for key, value in row.items()
                })
        return transactions
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except csv.Error as e:
        print(f"CSV reading error: {e}")
        return []


def read_excel_transactions(
    file_path: str = 'data/transactions_excel.xlsx'
) -> List[Dict]:
    """Чтение файла excel"""
    try:
        dataframe = pd.read_excel(file_path)
        transactions = dataframe.to_dict('records')

        transactions = [
            {key: _convert_value(value) for key, value in transaction.items()}
            for transaction in transactions
        ]

        return transactions
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"Excel reading error: {e}")
        return []


def _convert_value(value):
    """Преобразование значений для данных"""
    if isinstance(value, str):
        value = value.strip()
        try:
            return float(value.replace(',', '.'))
        except ValueError:
            pass

    return value
