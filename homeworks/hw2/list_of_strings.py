# Создаем пустой список для хранения строк
strings_list = []

# Запрашиваем ввод строк 10 раз
for i in range(10):
    user_input = input(f"Введите строку {i + 1}: ")

    # Проверяем, является ли последнее слово цифрой
    words = user_input.split()
    if words and words[-1].isdigit():
        position = int(words[-1])
        # Если позиция больше размера списка, добавляем в конец
        if position >= len(strings_list):
            strings_list.append(' '.join(words[:-1]))
        else:
            strings_list.insert(position, ' '.join(words[:-1]))
    else:
        # Если нет цифры, добавляем в конец списка
        strings_list.append(user_input)

# Выводим список на экран
print("Введенные строки:")
print(strings_list)