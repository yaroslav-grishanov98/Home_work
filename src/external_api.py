import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_exchange_rate(currency_code):
    """Получает текущий курс валюты к рублю с помощью API."""
    api_key = os.getenv("EXCHANGE_API_KEY")
    url = "http://api.apilayer.com/exchangerates_data/convert"

    params = {
        "from": currency_code,
        "to": "RUB",
        "amount": 1
    }

    headers = {
        "apikey": api_key
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if "result" in data:
                return data["result"]
        return None
    except Exception:
        return None
