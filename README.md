# Проект - Bank
## Описание:
Bank - это проект для синхронизирования банковских операций

## Установка:
1. Клонируйте репозиторий:
git clone https://github.com/yaroslav-grishanov98/Home_work
2. Установите зависимости:
pip install -r requirements.txt
## Использование:
from src.processing.py import filter_by_state, sort_by_date

# Пример использования filter_by_state
transactions = [ {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'} ] executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)


# Фильтрация транзакций по валюте USD
usd_transactions = list(filter_by_currency(transactions, "USD"))
print(usd_transactions)

# Пример использования функции filter_by_currency
 {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
          },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
         }
         ]

Фильтрация транзакций по валюте USD
usd_transactions = list(filter_by_currency(transactions, "USD"))
print(usd_transactions)

# Пример использования функции transaction_descriptions
descriptions = list(transaction_descriptions(transactions))
print(descriptions)

# Пример использования функции card_number_generator
card_numbers = list(card_number_generator(1, 5))
print(card_numbers)


**Тесты:**

* Проверяет извлечение описаний из списка транзакций.
* Тестирует случай с пустым списком транзакций.
* Проверяет обработку транзакций, у которых отсутствует описание.
* Использует @pytest.fixture для предоставления тестовых данных (списка транзакций).

### card_number_generator(start, stop)
Функция генерирует отформатированные номера карт в заданном диапазоне.

**Тесты:**

* Проверяет генерацию номеров карт в заданном диапазоне.
* Тестирует генерацию с разными диапазонами чисел.
* Проверяет случай, когда start и stop равны (один номер в диапазоне).
* Проверяет, что функция правильно обрабатывает начальное значение 0.
* Использует @pytest.fixture для предоставления списка сгенерированных номеров карт.

**Тесты:**

 ### filter_by_currency
* Проверяет, что функция корректно фильтрует транзакции по заданной валюте.
* Проверяет, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.
* Убедитесь, что генератор не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций.

### transaction_descriptions
* Проверяет извлечение описаний из списка транзакций.
* Тестирует случай с пустым списком транзакций.
* Проверяет обработку транзакций, у которых отсутствует описание.

### card_number_generator
* Проверяет генерацию номеров карт в заданном диапазоне.
* Тестирует генерацию с разными диапазонами чисел.
* Проверяет случай, когда start и stop равны (один номер в диапазоне).
