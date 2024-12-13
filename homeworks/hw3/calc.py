def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else "Ошибка: деление на ноль"
    elif operation == '**':
        return num1 ** num2
    elif operation == '//':
        return num1 // num2 if num2 != 0 else "Ошибка: деление на ноль"
    elif operation == '%':
        return num1 % num2 if num2 != 0 else "Ошибка: деление на ноль"
    else:
        return "Ошибка: неверный знак операции"

while True:
    # Чтение ввода
    input_str = input("Введите два числа и знак операции между ними (пустая строка - выход ): ")

    if input_str.strip() == "":
        print("Выход из программы.")
        break

    num1_str, operation, num2_str = input_str.split()
    num1 = float(num1_str)
    num2 = float(num2_str)

    # Вычисление и вывод результата
    result = calculate(num1, num2, operation)
    print("Результат:", result)