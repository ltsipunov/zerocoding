import math

def main():
    # Запрашиваем количество сторон и длину стороны многоугольника
    n = int(input("Введите количество сторон (углов) правильного многоугольника: "))
    side = float(input("Введите длину стороны правильного многоугольника: "))

    # Вычисляем площадь
    area = (n * side ** 2) / (4 * math.tan(math.pi / n))

    # Вычисляем радиус вписанной окружности
    r_in = side / (2 * math.tan(math.pi / n))

    # Вычисляем радиус описанной окружности
    r_out = side / (2 * math.sin(math.pi / n))

    # Выводим результаты
    print(f"Площадь правильного многоугольника: {area:.2f}")
    print(f"Радиус вписанной окружности: {r_in:.2f}")
    print(f"Радиус описанной окружности: {r_out:.2f}")

if __name__ == "__main__":
    main()