def bank(a, years):
    interest_rate = 0.10  # 10% годовых
    total_amount = a  # Начальная сумма вклада

    for year in range(years):
        total_amount += total_amount * interest_rate  # Увеличиваем сумму на 10%

    return total_amount  # Возвращаем итоговую сумму

# Пример использования функции
initial_deposit = float(input("Введите сумму вклада (в рублях): "))
investment_years = int(input("Введите срок вклада (в годах): "))

final_amount = bank(initial_deposit, investment_years)
print(f"Сумма на счету после {investment_years} лет составит: {final_amount:.2f} рублей")