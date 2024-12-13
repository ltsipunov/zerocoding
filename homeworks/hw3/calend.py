import calendar
from datetime import datetime
month_names = [
    "январь", "февраль", "март", "апрель", "май", "июнь","июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"
]

while True:
    # Запрос ввода
    user_input = input("Введите номер месяца и год (например, 3 2023) или нажмите Enter для выхода: ")

    # Проверка на пустую строку для выхода из цикла
    if user_input.strip() == "":
        print("Завершение программы")
        break

    # Разделение ввода
    parts = user_input.split()

    # Получение номера месяца
    month = int(parts[0])

    # Получение года, если он указан, иначе используем текущий год
    year = int(parts[1]) if len(parts) > 1 else datetime.now().year

    # Получение названия месяца
    month_name = month_names[ month - 1 ].capitalize()
    # Получение количества дней в месяце
    days_in_month = calendar.monthrange(year, month)[1]

    # Вывод результата
    print(f"{month_name} {year} содержит {days_in_month} дней.")