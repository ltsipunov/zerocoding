def find_minimum_of_three(numbers):
    """Находит минимум среди трех чисел."""
    if len(numbers) < 3:
        return None
    min_number = numbers[0]
    for num in numbers:
        if num < min_number:

            min_number = num
    return min_number

while True:
    user_input = input("Введите три числа, разделенных пробелами (или ничего для выхода): ")

    # Проверяем, пустая ли строка
    if user_input.strip() == "":
        print("Выход из программы.")
        break

    # Преобразуем строку в список чисел
    try:
        numbers = list(map(float, user_input.split()))
    except ValueError:
        print("Ошибка: введены некорректные данные. Попробуйте снова.")
        continue

    # Проверяем, что введено 3 числа
    if len(numbers) != 3:
        print("Ошибка: необходимо ввести ровно три числа.")
        continue

    # Находим минимум и выводим результат
    minimum = find_minimum_of_three(numbers)
    print("Минимум из введенных чисел:", minimum)
