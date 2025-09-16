___author___ = "Kuvykin N.D"

import numpy as np

#todo переделать на ndarray
def normalize_data(data) -> np.ndarray:
    """
    Нормализует данные по формуле: (x - min) / (max - min)
    Возвращает список нормализованных значений.
    """
    if not data:
        return []
    
    min_val = np.min(data)
    max_val = np.max(data)
    
    # Если все значения одинаковые, возвращаем список из 0
    if max_val == min_val:
        return (data * 0)
    
    # normalized = [(data - min_val) / np.ptp(data)]
    return ((data - min_val) / np.ptp(data))

def calculate_normalized_sum(data) -> np.ndarray:
    """
    Вычисляет сумму нормализованных значений списка.
    """
    normalized_data = normalize_data(data)
    return (np.sum(normalized_data))