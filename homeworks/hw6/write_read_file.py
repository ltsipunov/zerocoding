# Создаем пустой файл user_data.txt
filename = 'user_data.txt'

# Открываем файл в режиме записи (создаст файл, если он не существует)
with open(filename, 'w', encoding='utf-8') as file:
    print("Введите строки для сохранения в файл. Чтобы выйти, введите пустую строку.")

    while True:
        user_input = input("Введите строку: ")

        # Проверяем, является ли строка пустой
        if user_input == "":
            break

        # Записываем строку в файл
        file.write(user_input + '\n')

# После выхода из цикла, открываем файл в режиме чтения и выводим его содержимое
with open(filename, 'r', encoding='utf-8') as file:
    print("\nСодержимое файла user_data.txt:")
    print(file.read())