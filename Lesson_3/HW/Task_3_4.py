# 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import random


def print_list(n):
    new_list = []
    for i in range(0, n):
        new_list.append(round(random.uniform(0, 10), 2))
    print(new_list)
    list_int = []
    for i in range(0, n):
        a = round((new_list[i]-int(new_list[i])), 2)
        list_int.append(a)
    return list_int


def max_min_difference(list_2, n):
    min_num = list_2[0]
    max_num = list_2[0]
    for i in range(1, n):
        if list_2[i] > max_num:
            max_num = list_2[i]
        if list_2[i] < min_num:
            min_num = list_2[i]
    print('Max: ', max_num)
    print('Min: ', min_num)
    result = max_num-min_num
    return (result)


n = int(input("Input number: "))
list_1 = print_list(n)
print(list_1)
print('Difference: ', max_min_difference(list_1, n))
