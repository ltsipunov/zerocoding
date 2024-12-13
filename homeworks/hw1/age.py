from datetime import datetime


def calculate_age(birth_date):
    today = datetime.now()
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day
    age_hours = today.hour - birth_date.hour
    age_minutes = today.minute - birth_date.minute
    age_seconds = today.second - birth_date.second

    # Корректируем значения, если необходимо
    if age_seconds < 0:
        age_seconds += 60
        age_minutes -= 1
    if age_minutes < 0:
        age_minutes += 60
        age_hours -= 1
    if age_hours < 0:
        age_hours += 24
        age_days -= 1
    if age_days < 0:
        # Получаем количество дней в предыдущем месяце
        if today.month == 1:
            last_month = 12
            last_month_year = today.year - 1
        else:
            last_month = today.month - 1
            last_month_year = today.year

        last_month_days = (datetime(last_month_year, last_month, 1) - datetime(last_month_year, last_month - 1, 1)).days
        age_days += last_month_days
        age_months -= 1
    if age_months < 0:
        age_months += 12
        age_years -= 1

    return age_years, age_months, age_days, age_hours, age_minutes, age_seconds


def main():
    # Запрашиваем имя пользователя
    name = input("Введите ваше имя: ")

    # Запрашиваем дату рождения
    birth_date_str = input("Введите вашу дату рождения (гггг-мм-дд): ")

    # Преобразуем строку в объект даты
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")

    # Вычисляем возраст
    age = calculate_age(birth_date)

    # Выводим результат
    print(
        f"Привет {name}! Тебе {age[0]} лет, {age[1]} месяцев, {age[2]} дней, {age[3]} часов, {age[4]} минут и {age[5]} секунд.")


if __name__ == "__main__":
    main()