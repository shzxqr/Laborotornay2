import random
from math_operations import (
    calculate_standard_deviation,
    calculate_median,
    calculate_geometric_mean
)


def generate_random_numbers(count=5):
    """Функция генерации списка случайных чисел"""
    return [random.randint(1, 100) for _ in range(count)]


def calculate_average(numbers):
    """Функция вычисления среднего арифметического"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def main():
    print("=== Программа математических вычислений ===")

    # Генерируем больше случайных чисел
    numbers = generate_random_numbers(7)
    print(f"Сгенерированные числа: {numbers}")

    # Базовые вычисления
    avg = calculate_average(numbers)
    print(f"\nБазовые вычисления:")
    print(f"Среднее арифметическое: {avg:.2f}")
    print(f"Минимальное число: {min(numbers)}")
    print(f"Максимальное число: {max(numbers)}")

    # Расширенные вычисления (новый функционал)
    print(f"\nРасширенные вычисления:")

    std_dev = calculate_standard_deviation(numbers)
    print(f"Стандартное отклонение: {std_dev:.2f}")

    median = calculate_median(numbers)
    print(f"Медиана: {median:.2f}")

    geo_mean = calculate_geometric_mean(numbers)
    if geo_mean:
        print(f"Среднее геометрическое: {geo_mean:.2f}")
    else:
        print("Среднее геометрическое не может быть вычислено")


if __name__ == "__main__":
    main()