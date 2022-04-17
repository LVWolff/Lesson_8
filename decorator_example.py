# простые декораторы

def show_info(f):
    def wrapper():
        print('Код до функции')
        f()
        print('Код после функции')
    return wrapper

def simple_func():
    print('я простая функция')

@show_info
def simple_func_2():
    print('я простая функция №2')

simple_func()

simple_func_decor = show_info(simple_func)
simple_func_decor()

simple_func_2()

#Декораторы с параметрами

def show_type(f):
    def wrapper(*args, **kwargs):
        print('Код до функции', type(args[0]))
        print(f(*args, **kwargs))
        print('Код после функции', type(args[1]))
    return wrapper

def show_info2(f):
    def wrapper(*args, **kwargs):
        print('Код до функции')
        f(*args, **kwargs)
        print('Код после функции')
    return wrapper

@show_info2
@show_type
def my_add(a,b):
    return a+b

my_add(3,2)

# пример использования декоратора

import time
import requests

def show_time(f):
    def wrapper(*args, **kwargs):
        print(time.time())
        print('URL:', *args)
        print(f(*args, **kwargs))
        print(time.time())
    return wrapper

@show_time
def request_example(url):
    webpage = requests.get(url)
    return webpage.text

url = 'https://ya.ru'
request_example(url)
