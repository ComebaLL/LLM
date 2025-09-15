___author___ = "Kuvykin N.D"

from collecl_creator import *
from write_in_file import *
from func_norm import *

def main(*args, **kwargs):
    """
    Создать набор из случайных чисел бех повторов x1,x2,...,xn. 
    Интервал случайных значений (a,b) и кол-во случайных чисел
    задаются пользователем n << b - a.
    """

    x = input("набор 1 n = 10**3, a = 0, b = 10**4\n" \
              "набор 2 n = 10**6, a = 0, b = 10**7\n")
    if x == "1":
        n = 10**3
        a = 0
        b = 10**4
    elif x == "2":
        n = 10**6
        a = 0
        b = 10**7

    list_cllection = unique_list_creator(n, a, b)
    set_cllection = unique_set_creator(n, a, b)
    ndarray_cllection = unique_ndarray_creator(n, a, b)

    list_normal_sum = calculate_normalized_sum(list_cllection)

    print(list_normal_sum)

    write_to_csv("output", list_cllection=list_cllection)


if __name__ == "__main__":
    main()


        