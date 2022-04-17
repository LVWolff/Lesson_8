import sys

simple_list = [i**3 for i in range(100)]
print(type(simple_list))

# for i in simple_list:
#     print(i)

print('Mem_1', sys.getsizeof(simple_list))

# неявный генератор

simple_generator = (x**3 for x in range(100))
print(type(simple_generator))
# for i in simple_generator:
#     print(i)

print('Mem_2', sys.getsizeof(simple_generator))

#явные генераторы

#Простой  пример
def generator_example(num):
    for i in range(num):
        yield (i**3)

gen = generator_example(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


#сложный генератр
import time
import os
import random
import psutil

colors = ['White', 'Black', 'Green']
brands = ['Volvo', 'Nissan', 'Lada']

# без генератора
print("----------------")
print("Без генератора")
def cars(num):
    cars_list = []
    for i in range(num):
        car = {'color': random.choice(colors),
               'brand': random.choice(brands),
               'id': i}
        cars_list.append(car)
    return cars_list

proc = psutil.Process(os.getpid())
print('Используемая память до выполнения функции: ' + str(proc.memory_info().rss/1000000))
start = time.perf_counter()

cars_list = cars(1000000)
# print(cars_list)
stop = time.perf_counter()

proc = psutil.Process(os.getpid())
print('Используемая память после выполнения функции: ' + str(proc.memory_info().rss/1000000))
print("Заняло {} секунд".format(stop - start))


#при использовании генератора

print("----------------")
print("C генератором")

def cars_gen(num):
    for i in range(num):
        car = {'color': random.choice(colors),
               'brand': random.choice(brands),
               'id': i}
        yield car

proc = psutil.Process(os.getpid())
print('Используемая память до выполнения функции: ' + str(proc.memory_info().rss/1000000))
start = time.perf_counter()

cars_list = cars_gen(1000000)
# print(cars_list)
stop = time.perf_counter()

proc = psutil.Process(os.getpid())
print('Используемая память после выполнения функции: ' + str(proc.memory_info().rss/1000000))
print("Заняло {} секунд".format(stop - start))
