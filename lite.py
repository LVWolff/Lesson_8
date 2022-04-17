# 1. Написать декоратор, замеряющий время выполнение декорируемой функции.
# 2. Сравнить время создания генератора и списка с элементами: натуральные числа
#     от 1 до 1000000 (создание объектов оформить в виде функций).

import time

def show_time(f):
    def wrapper(*args, **kwargs):
        print('----------------')
        print('Генерация списка с помощью:', args[1])
        start = time.perf_counter()
        result = f(*args, **kwargs)
        stop = time.perf_counter()
        print('Выполнение заняло {} сек'.format(stop - start))
        return result
    return wrapper

@show_time
def make_list_nat_num(n, title):
    return [i for i in range(1,n+1)]

@show_time
def make_generator_nut_num(n, title):
    for i in range(1, n+1):
        yield i

list_n = make_list_nat_num(1000000, 'формирования списка')
print(type(list_n))
list_n_gen = make_generator_nut_num(1000000, 'формирования генератора')
print(type(list_n_gen))

