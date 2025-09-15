___author___ = "Kuvykin N.D"

import time
import functools
from write_in_file import write_to_md

def time_dec(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() # время начала выполнения
        # выполняем оригинальную функцию с переданными аргументами
        value = func(*args, **kwargs)    
        end_time = time.perf_counter()   # время окончания выполнения
        run_time = end_time - start_time  # время выполнения функции
        write_to_md(func.__name__, run_time) # запись в marckdown файл
        return value
    return wrapper_timer