def print_even_numbers(start,end):
    # Инициализируем список для четных чисел
    even_numbers = []

    # Проходим по всем числам в заданном диапазоне
    for num in range(start, end + 1):
        if num % 2 == 0:  # Проверяем, является ли число четным
            even_numbers.append(num)  # Добавляем четное число в список
    # Выводим четные числа в одной строке
    print("Четные числа в диапазоне от", start, "до", end, ":", ', '.join(map(str, even_numbers)))

while True:
    input_str = input("Введите два числа через пробел: ")
    # Разбиваем строку на части
    parts = input_str.split()
    if not parts: break

    # Проверяем, что введено ровно 2 числа
    if len(parts) != 2:
        print("Ошибка: необходимо ввести ровно два числа.")
        continue
    try:
        # Преобразуем строки в числа
        num1 = int(parts[0])
        num2 = int (parts[1])
        if num2 > num1:
            print_even_numbers(num1, num2)
        else:
            print("Ошибка: второе число должно быть больше первого.")
    except ValueError:
        print("Ошибка: оба значения должны быть числами.")