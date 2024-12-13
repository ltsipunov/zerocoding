import random

def sum_of_random_numbers(size, lower_bound, upper_bound):
    numbers = [random.randint(lower_bound, upper_bound) for _ in range(size)]
    total = sum(numbers)  # Суммируем числа с помощью встроенной функции sum
    return numbers, total

print("Для выхода из программы нажмите ПРОБЕЛ.")

while True:
    # Запрос размера списка у пользователя
    size_input = input("Введите размер списка (или нажмите ПРОБЕЛ для выхода): ")

    if size_input == ' ':  # Проверяем, был ли введен ПРОБЕЛ
        print("Выход из программы.")
        break

    try:
        size = int(size_input)  # Преобразуем ввод в целое число
        lower_bound = 1  # Нижний предел
        upper_bound = 100  # Верхний предел

        random_numbers, total = sum_of_random_numbers(size, lower_bound, upper_bound)
        print(f"Случайные числа: {random_numbers}")
        print(f"Сумма чисел: {total}\n")
    except ValueError:
        print("Пожалуйста, введите целое число для размера списка.")