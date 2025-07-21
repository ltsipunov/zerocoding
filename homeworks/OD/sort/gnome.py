def sort(arr):
# - Алгоритм сравнивает текущий элемент с предыдущим.
# - Если порядок правильный, переходит к следующему элементу.
# - Если нет — меняет их местами и возвращается назад на один шаг.
# - Повторяет процесс, пока не пройдет весь массив.
    index = 0
    n = len(arr)
    while index < n:
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr
