import os
from typing import Dict, List

from src.decorators import log
from src.filter_transactions import filter_transactions_by_description
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


@log(file_name="operations.log")
def main() -> None:
    """Основная логика программы для работы с банковскими транзакциями."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input()
        if choice == '1':
            file_path = "operations.json"
            print("\nДля обработки выбран JSON-файл.")
            break
        print("В текущей версии поддерживается только JSON формат.")

    transactions = load_transactions(file_path)

    while True:
        print("\nВведите статус для фильтрацию.")
        print("Доступные статусы: EXECUTED, CANCELED, PENDING")

        status = input().upper()
        if status in ['EXECUTED', 'CANCELED', 'PENDING']:
            filtered_transactions = filter_by_state(transactions, status)
            print(f'\nОперации отфильтрованы по статусу "{status}"')
            break
        print(f'\nСтатус операции "{status}" недоступен.')

    sort_answer = input("\nОтсортировать операции по дате? Да/Нет\n").lower()
    if sort_answer == 'да':
        sort_direction = input("\nОтсортировать по возрастанию или по убыванию?\n").lower()
        reverse_order = sort_direction == 'по убыванию'
        filtered_transactions = sort_by_date(filtered_transactions, reverse_order)

    currency_answer = input("\nВыводить только рублевые транзакции? Да/Нет\n").lower()
    if currency_answer == 'да':
        filtered_transactions = list(filter_by_currency(filtered_transactions, 'RUB'))

    description_answer = input("\nОтфильтровать список транзакций по определенному слову "
                               "в описании? Да/Нет\n").lower()
    if description_answer == 'да':
        search_word = input("Введите слово для поиска: ")
        filtered_transactions = filter_transactions_by_description(
            filtered_transactions,
            search_word
        )

    print("\nРаспечатываю итоговый список транзакций...")

    if not filtered_transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}\n")

    for transaction in filtered_transactions:
        date = get_date(transaction['date'])
        description = transaction['description']

        from_account = transaction.get('from', '')
        to_account = transaction['to']

        if from_account:
            from_masked = mask_account_card(from_account)
            to_masked = mask_account_card(to_account)
            account_info = f"{from_masked} -> {to_masked}"
        else:
            account_info = mask_account_card(to_account)

        amount = transaction['operationAmount']['amount']
        currency = transaction['operationAmount']['currency']['code']

        print(f"{date} {description}")
        print(account_info)
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
