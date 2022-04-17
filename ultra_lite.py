# 1. Написать свой генератор последовательностей, свой тернарный оператор
# 2. Написать свой декоратор


#генератор формирования четных чисел

n = 99
list_even_num = [i for i in range(1,n+1) if i%2 == 0]
print(list_even_num)

# тернарный оператор
is_even_num = True if n%2 == 0 else False
print(is_even_num)

def show_list(f):
    def wrapper(*args, **kwargs):
        print('Поиск всех четных чисел от 1 до', args[0])
        temp_list = f(*args, **kwargs)
        print('Процесс завершен. Длина списка:', len(temp_list))
    return wrapper

@show_list
def gen_even_num(x):
    list_even_num = [i for i in range(1, x + 1) if i % 2 == 0]
    print(list_even_num)
    return list_even_num

gen_even_num(100)