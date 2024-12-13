def main():
    # Запрашиваем ввод двух чисел
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    # Выполняем арифметические операции
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "Ошибка: деление на ноль"
    floor_division = num1 // num2 if num2 != 0 else "Ошибка: деление на ноль"
    modulus = num1 % num2 if num2 != 0 else "Ошибка: деление на ноль"
    exponentiation = num1 ** num2

    # Выводим результаты
    print(f"Сумма: {addition}")
    print(f"Разность: {subtraction}")
    print(f"Произведение: {multiplication}")
    print(f"Частное: {division}")
    print(f"Целочисленное деление: {floor_division}")
    print(f"Остаток от деления: {modulus}")
    print(f"Возведение в степень: {exponentiation}")

if __name__ == "__main__":
    main()
