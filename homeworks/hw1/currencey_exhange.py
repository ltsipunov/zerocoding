import requests

def get_exchange_rate():
    # URL API для получения курсов валют
    url = 'https://api.exchangerate-api.com/v4/latest/RUB'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['rates']['USD']
    else:
        print("Ошибка при получении данных о курсе. Попробуйте позже.")
        return None


def main():
    # Запрашиваем сумму в рублях
    rub_amount = float(input("Введите сумму в рублях: "))

    # Получаем текущий курс доллара
    exchange_rate = get_exchange_rate()
    print(f"Получен курс обмена: {exchange_rate:.4f} USD за 1 RUB")

    if exchange_rate is not None:
        # Конвертируем рубли в доллары
        dollar_amount = rub_amount * exchange_rate

        print(f"Сумма в долларах: {dollar_amount:.2f} USD")


if __name__ == "__main__":
    main()