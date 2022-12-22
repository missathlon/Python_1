# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4
# out
# [4, 2, 4, 9]
# 8

from random import sample


def num_sum(a):
    new_list = sample(range(1, a*5), k=a)
    print(new_list)
    sum = 0
    for i in range(0, a, 2):
        sum += new_list[i]
    print(sum)


a = int(input("Input number: "))
num_sum(a)
