from utils.file_operations import read_transactions
from external_api.currency_converter import convert_to_rubles


def main():
    transactions = read_transactions('data/operations.json')
    """Чтение транзакций из файла"""
    if not transactions:
        print("Нет данных для обработки.")
        return

    """Обработка каждой транзакции и конвертация валюты"""
    for transaction in transactions:
        currency = transaction.get('currency')
        amount = transaction.get('amount')

        if currency and amount is not None:
            amount_in_rubles = convert_to_rubles(currency, amount)
            if amount_in_rubles is not None:
                print(f"Сумма транзакции в рублях: {amount_in_rubles}")
            else:
                print(f"Не удалось конвертировать валюту {currency} для суммы {amount}")
        else:
            print("Некорректные данные транзакции")


print(convert_to_rubles())
if __name__ == "__main__":
    main()
