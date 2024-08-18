def sum_range(start, end):
    # Проверяем, что start меньше или равен end
    if start > end:
        return 0  # Если start больше end, возвращаем 0

    total = 0
    for number in range(start, end + 1):
        total += number  # Суммируем каждое число в диапазоне
    return total


# Пример использования функции
start_value = int(input("Введите начальное значение (start): "))
end_value = int(input("Введите конечное значение (end): "))

result = sum_range(start_value, end_value)
print(f"Сумма всех целых чисел от {start_value} до {end_value} включительно: {result}")