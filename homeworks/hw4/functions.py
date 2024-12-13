import math
sum_range = lambda start, end: sum(range(int(start), int(end) + 1))
square = lambda side: (4 * side, side ** 2, round( side * math.sqrt(2),3)  )
bank = lambda a, years, proc=10: round( a * ((1 + proc / 100) ** years), 3)

while True:
    user_input = input("Введите имя функции и аргументы (или пустую строку для выхода): ").strip()

    if user_input == "":
        break  # Выход из цикла при вводе пустой строки

    parts = user_input.split()
    func_name = parts[0]
    args = list(map(float, parts[1:]))  # Преобразуем аргументы в числа (при необходимости)

    # Проверяем, существует ли функция в глобальной таблице
    if func_name in "sum_range square bank".split():
        try:
            result = locals()[func_name](*args)  # Вызов функции с распаковкой аргументов
            print(f"Результат: {result}")
        except TypeError as e:
            print(f"Ошибка: некорректное количество аргументов для функции '{func_name}': {e}")
    else:
        print(f"Ошибка: функция '{func_name}' не найдена.")