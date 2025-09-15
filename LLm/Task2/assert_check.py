___author___ = "Kuvykin N.D"


import math

from func_norm import normalize_data, calculate_normalized_sum

def test_normalize_data_empty_list():
    """Тест пустого списка"""
    assert normalize_data([]) == []

def test_normalize_data_single_element():
    """Тест списка с одним элементом"""
    assert normalize_data([5]) == [1.0]
    assert normalize_data([0]) == [1.0]
    assert normalize_data([-10]) == [1.0]

def test_normalize_data_identical_values():
    """Тест списка с одинаковыми значениями"""
    assert normalize_data([7, 7, 7, 7]) == [1.0, 1.0, 1.0, 1.0]
    assert normalize_data([0, 0, 0]) == [1.0, 1.0, 1.0]
    assert normalize_data([-5, -5, -5]) == [1.0, 1.0, 1.0]

def test_normalize_data_positive_numbers():
    """Тест положительных чисел"""
    data = [10, 20, 30, 40, 50]
    result = normalize_data(data)

    # Ожидаемый результат после нормализации:
    # Формула: (x - min) / (max - min)
    # min = 10, max = 50, диапазон = 40 
    # 10 -> (10-10)/40 = 0/40 = 0.0
    # 20 -> (20-10)/40 = 10/40 = 0.25
    # 30 -> (30-10)/40 = 20/40 = 0.5
    # 40 -> (40-10)/40 = 30/40 = 0.75
    # 50 -> (50-10)/40 = 40/40 = 1.0
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    
    # Поэлементное сравнение с учетом погрешности вычислений с плавающей точкой
    for result_value, expected_value in zip(result, expected):
        assert math.isclose(result_value, expected_value, abs_tol=1e-10)

def test_calculate_normalized_sum_identical():
    """Тест суммы для одинаковых значений"""
    assert calculate_normalized_sum([7, 7, 7]) == 3.0
    assert calculate_normalized_sum([0, 0, 0, 0]) == 4.0

def test_calculate_normalized_sum_linear():
    """Тест суммы для линейной последовательности"""
    # Для [0, 1, 2, 3, 4] нормализованные: [0.0, 0.25, 0.5, 0.75, 1.0]
    # Сумма = 0 + 0.25 + 0.5 + 0.75 + 1.0 = 2.5
    assert math.isclose(calculate_normalized_sum([0, 1, 2, 3, 4]), 2.5, abs_tol=1e-10)
    
    # Для [10, 20, 30, 40, 50] нормализованные: [0.0, 0.25, 0.5, 0.75, 1.0]
    assert math.isclose(calculate_normalized_sum([10, 20, 30, 40, 50]), 2.5, abs_tol=1e-10)

def test_calculate_normalized_sum_symmetry():
    """Тест для положительных и отрицательных чисел"""
    positive = [10, 20, 30, 40, 50]
    negative = [-50, -40, -30, -20, -10]
    
    sum_positive = calculate_normalized_sum(positive)
    sum_negative = calculate_normalized_sum(negative)
    
    assert math.isclose(sum_positive, sum_negative, abs_tol=1e-10)