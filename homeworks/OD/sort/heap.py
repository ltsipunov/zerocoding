def heapify(arr, n, i):
    """
    Восстанавливает свойство кучи для поддерева с корнем в узле i,
    при этом n — размер кучи.
    """
    largest = i  # Изначально предполагаем, что корень — наибольший
    left = 2 * i + 1  # левый дочерний узел
    right = 2 * i + 2  # правый дочерний узел

    # Если левый дочерний узел больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый дочерний узел больше текущего наибольшего
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # меняем местами
        # Восстанавливаем свойство кучи для дочернего узла
        heapify(arr, n, largest)


def sort(arr):
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлекаем элементы из кучи по одному
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # переносим текущий максимум в конец
        heapify(arr, i, 0)  # восстанавливаем свойство кучи для оставшейся части
    return arr
