# тернарный оператор

age = 20

def check_adult(age):
    check = 0
    if age >= 18:
        check = 1
    else:
        check = 0
    return check

check_adult_l = lambda x: 1 if x >= 18 else 0

check = 1 if age >= 18 else 0 # тернальный оператор (!)

print(check_adult(age))
print(check)
print(check_adult_l(age))

# генератор последовательности

list_sqr  = []
list_sqr2 = []
n = 10

for i in range(1, n+1):
    list_sqr.append((i ** 2))
    list_sqr2.append((i**2)%10)

print(list_sqr)
print(list_sqr2)

list_sqr_g = [(i ** 2) for i in range(1, n+1)]
list_sqr_g_2 = [(i ** 2)%10 for i in range(1, n+1)]
print(list_sqr_g)
print(list_sqr_g_2)

list_sqr_2_1 = []
list_sqr_2_2 = []


for i in range(1, n+1):
    if (i**2)%2 == 0:
        list_sqr_2_1.append((i ** 2))
        list_sqr_2_2.append((i**2)%10)
print(list_sqr_2_1)
print(list_sqr_2_2)

list_sqr_g_2_1 = [(i**2) for i in range(1, n+1) if (i**2)%2 == 0]
list_sqr_g_2_2 = [(i**2)%10 for i in range(1, n+1) if (i**2)%2 == 0]
print(list_sqr_g_2_1)
print(list_sqr_g_2_2)

# генератор для словаря

dict_g = {i:i**2 for i in range(1, n+1)}
print(dict_g)

# множество

set_g = {i**2 for i in range(1, n+1)}
set_g_d = {(i**2)%10 for i in range(1, n+1)}
print(set_g)
print(set_g_d)

# Задачи
list_names = ['Dima', 'kate', 'Oleg', 'natali']

#сформировать список из первых букв так, чтобы они были заглавные

list_chars = [x[0] if x[0].isupper() else x[0].title() for x in list_names]
print(list_chars)


