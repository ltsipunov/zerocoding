# Example of ValueError interceptipon
def get_integer_input():
    while True:
        user_input = input("Введите целое число (выход из программы -  ENTER): ")
        if not user_input:
            break
        try:
            number = int(user_input)
            print(f"Вы ввели целое число: {number}")
        except ValueError:
            print("Невозможно преобразовать введенное значение в целое число. Попробуйте еще раз.")

# Запускаем функцию
get_integer_input