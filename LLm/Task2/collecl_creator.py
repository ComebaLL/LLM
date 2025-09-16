___author___ = "Kuvykin N.D"

import random
import numpy as np
from time_dec import time_dec

@time_dec
def unique_list_creator(n: float, a: float, b: float) -> list:
    """
    Создать набор из случайных чисел бех повторов x1,x2,...,xn. 
    Интервал случайных значений (a,b) и кол-во случайных чисел
    задаются пользователем n << b - a.
    """

    # проверка интервала
    if n >= (b - a) // 2:
        raise ValueError(f"ошибка n ({n}) большое")
    if n < 0:
        raise ValueError(f"ошибка n ({n}) меньше нуля")

    # список для результата
    result = []

    while len(result) < n:
        num = random.randint(a, b) # генерация случайного числав интервале

        if num % 2 == 0 and num not in result: # проверяем что число четное и его нет в списке
            result.append(num)
    
    return result

@time_dec
def unique_set_creator(n: float, a: float, b: float) -> set:
    """
    Создать набор из случайных чисел бех повторов x1,x2,...,xn. 
    Интервал случайных значений (a,b) и кол-во случайных чисел
    задаются пользователем n << b - a.
    """

    # проверка интервала
    if n >= (b - a) // 2:
        raise ValueError(f"ошибка n ({n}) большое")
    if n < 0:
        raise ValueError(f"ошибка n ({n}) меньше нуля")

    # список для результата
    unique_set = set()

    while len(unique_set) < n:
        num = random.randint(a, b) # генерация случайного числав интервале

        if num % 2 == 0: # проверяем что число четное и его нет в списке
            unique_set.add(num)
    
    result = list(unique_set)

    return result

@time_dec
def unique_ndarray_creator(n: float, a: float, b: float) -> np.ndarray:
    """
    Создать набор из случайных чисел бех повторов x1,x2,...,xn. 
    Интервал случайных значений (a,b) и кол-во случайных чисел
    задаются пользователем n << b - a.
    """

    # проверка интервала
    if n >= (b - a) // 2:
        raise ValueError(f"ошибка n ({n}) большое")
    if n < 0:
        raise ValueError(f"ошибка n ({n}) меньше нуля")

    # список для результата
    result = []

    # Создаем все четные числа в интервале
    # проверку размера от start до end чтобы размер был в "размуных" пределах
    if n <= 10**6:
        start = a if a % 2 == 0 else a + 1
        end = b if b % 2 == 0 else b - 1
        all_even_numbers = np.arange(start, end + 1, 2)
        result = np.random.choice(all_even_numbers, size = n, replace = False)
    else:
        while len(result) < n:
            num = random.randint(a, b) # генерация случайного числав интервале

        if num % 2 == 0 and num not in result: # проверяем что число четное и его нет в списке
            result.append(num)
        result = np.random.choice(all_even_numbers, size = n, replace = False)
    
    return result