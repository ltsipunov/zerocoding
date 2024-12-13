from arithmetic import add,sub,mul,div
opers= { '+':add, '-':sub, '*':mul, '/':div}

def calculate(num1, num2, op):
    if op in '+-*/':
        return opers[op](num1,num2)
    else:
        return "Ошибка: неверный знак операции"

while True:
    # Чтение ввода
    input_str = input("Введите два числа и знак операции между ними (пустая строка - выход ): ")
    try:
        if input_str.strip() == "":
            print("Выход из программы.")
            break

        a =  input_str.split()
        if len(a) != 3:
            print('Строка должна содержить число, знак операции и число, разделнные пробелами')
            continue
        num1_str, operation, num2_str =  a
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError as e:
            print(e)
            continue

        # Вычисление и вывод результата
        result = calculate(num1, num2, operation)
        print("Результат:", result)
    except ZeroDivisionError:
        print('Делить на 0 нельзя!')
