def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Примеры использования функции
for x,y in [ [10,2],[5,0], [7,3],[4,-1], [0,9], [13,0] ] :
    print(f"Делим {x} на {y} , результат  {safe_divide(x,y)}" )