import math
def square(side):
    # Вычисление периметра, площади и диагонали квадрата
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    return perimeter, area, diagonal  # Возвращаем значения в виде кортежа

# Пример использования функции
side_length = float(input("Введите длину стороны квадрата: "))

perimeter, area, diagonal = square(side_length)
print(f"Периметр квадрата: {perimeter}")
print(f"Площадь квадрата: {area}")
print(f"Диагональ квадрата: {diagonal:.2f}")  # Форматируем вывод диагонали до двух знаков после запятой