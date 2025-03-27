import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_exchange_rate(currency_code):
    """Получает текущий курс валюты к рублю с помощью API."""
    api_key = os.getenv('EXCHANGE_API_KEY')  # Читаем ключ из переменных окружения
    url = f"http://api.apilayer.com/exchangerates_data/latest?base=RUB&symbols={currency_code}"

    headers = {
        "apikey": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'rates' in data and currency_code in data['rates']:
            return data['rates'][currency_code]
        else:
            return None
    else:
        return None
