___author___ = "Kuvykin N.D"


def normalize_data(data: list[float]) -> list[float]:
    """
    Нормализует данные по формуле: (x - min) / (max - min)
    Возвращает список нормализованных значений.
    """
    if not data:
        return []
    
    min_val = min(data)
    max_val = max(data)
    
    # Если все значения одинаковые, возвращаем список из 1.0
    if max_val == min_val:
        return [1.0] * len(data)
    
    normalized = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized

def calculate_normalized_sum(data: list[float]) -> float:
    """
    Вычисляет сумму нормализованных значений списка.
    """
    normalized_data = normalize_data(data)
    return sum(normalized_data)