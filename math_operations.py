import math


def calculate_standard_deviation(numbers):
    """Функция вычисления стандартного отклонения"""
    if len(numbers) < 2:
        return 0

    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    return math.sqrt(variance)


def calculate_median(numbers):
    """Функция вычисления медианы"""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        # Четное количество элементов
        mid = n // 2
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        # Нечетное количество элементов
        return sorted_numbers[n // 2]


def calculate_geometric_mean(numbers):
    """Функция вычисления среднего геометрического"""
    if not numbers or 0 in numbers or any(x < 0 for x in numbers):
        return None

    product = 1
    for num in numbers:
        product *= num

    return product ** (1 / len(numbers))