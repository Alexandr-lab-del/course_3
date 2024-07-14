import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"


def convert_to_rubles(currency, amount):
    if currency == "RUB":
        return amount

    url = BASE_URL.format(to="RUB", from_currency=currency, amount=amount)
    headers = {
        "apikey": API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get('result', None)
    else:
        print(f"Ошибка при запросе к API: {response.status_code} - {response.text}")
        return None


print(f"API_KEY: {API_KEY}")
"""Проверка получения API ключа"""

"""Тестовый запрос к API для проверки корректности"""
url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
headers = {"apikey": API_KEY}
response = requests.get(url, headers=headers)
print(f"Статус-код: {response.status_code}")
print(f"Ответ: {response.text}")
