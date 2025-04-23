import csv
from typing import Dict, List, Any

import pandas as pd


def read_csv_transactions(file_path: str = 'data/transactions.csv') -> List[Dict]:
    """Чтение и преобразование данных из CSV-файла банковских транзакций"""
    try:
        transactions = []
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=';')
            for row in csv_reader:
                transaction = {
                    'id': row.get('id'),
                    'state': row.get('state'),
                    'date': row.get('date'),
                    'description': row.get('description'),
                    'from': row.get('from', ''),
                    'to': row.get('to'),
                    'operationAmount': {
                        'amount': _convert_value(row.get('amount')),
                        'currency': {
                            'name': row.get('currency_name'),
                            'code': row.get('currency_code')
                        }
                    }
                }
                transactions.append(transaction)
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
    """Чтение и преобразование данных из Excel-файла банковских транзакций"""
    try:
        dataframe = pd.read_excel(file_path, engine='openpyxl')
        raw_transactions = dataframe.to_dict('records')

        transactions = []
        for row in raw_transactions:
            transaction = {
                'id': row.get('id'),
                'state': row.get('state'),
                'date': row.get('date'),
                'description': row.get('description'),
                'from': row.get('from', ''),
                'to': row.get('to'),
                'operationAmount': {
                    'amount': _convert_value(row.get('amount')),
                    'currency': {
                        'name': row.get('currency_name'),
                        'code': row.get('currency_code')
                    }
                }
            }
            transactions.append(transaction)

        return transactions
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"Excel reading error: {e}")
        return []


def _convert_value(value: Any) -> Any:
    """Преобразование значений для корректного представления данных"""
    if isinstance(value, str):
        value = value.strip()
        try:
            return float(value.replace(',', '.'))
        except ValueError:
            pass

    return value
