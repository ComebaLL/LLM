___author___ = "Kuvykin N.D"

import numpy as np
import pytest

from func_norm import normalize_data, calculate_normalized_sum

def test_normalize_data_empty_list():
    """Тест пустого массива"""
    result = normalize_data(np.array([]))  
    assert isinstance(result, np.ndarray)
    assert result.size == 0

def test_normalize_data_single_element():
    """Тест массива с одним элементом"""
    assert np.allclose(normalize_data(np.array([5])), [0.0]) 
    assert np.allclose(normalize_data(np.array([0])), [0.0])
    assert np.allclose(normalize_data(np.array([-10])), [0.0])

def test_normalize_data_identical_values():
    """Тест массива с одинаковыми значениями"""
    assert np.allclose(normalize_data(np.array([7, 7, 7, 7])), [0.0, 0.0, 0.0, 0.0])
    assert np.allclose(normalize_data(np.array([0, 0, 0])), [0.0, 0.0, 0.0])
    assert np.allclose(normalize_data(np.array([-5, -5, -5])), [0.0, 0.0, 0.0])

def test_normalize_data_positive_numbers():
    """Тест положительных чисел"""
    data = np.array([10, 20, 30, 40, 50])  
    result = normalize_data(data)
    expected = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    assert np.allclose(result, expected, atol=1e-10)

def test_calculate_normalized_sum_identical():
    """Тест суммы для одинаковых значений"""
    assert calculate_normalized_sum(np.array([7, 7, 7])) == 0.0  
    assert calculate_normalized_sum(np.array([0, 0, 0, 0])) == 0.0
    assert calculate_normalized_sum(np.array([-5, -5, -5])) == 0.0

def test_calculate_normalized_sum_linear():
    """Тест суммы для линейной последовательности"""
    assert np.isclose(calculate_normalized_sum(np.array([0, 1, 2, 3, 4])), 2.5, atol=1e-10)
    assert np.isclose(calculate_normalized_sum(np.array([10, 20, 30, 40, 50])), 2.5, atol=1e-10)

def test_calculate_normalized_sum_symmetry():
    """Тест для положительных и отрицательных чисел"""
    positive = np.array([10, 20, 30, 40, 50])
    negative = np.array([-50, -40, -30, -20, -10])
    
    sum_positive = calculate_normalized_sum(positive)
    sum_negative = calculate_normalized_sum(negative)
    
    assert np.isclose(sum_positive, sum_negative, atol=1e-10)