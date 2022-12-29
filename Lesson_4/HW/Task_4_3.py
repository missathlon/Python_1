# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
# Negative value of the number of numbers!
# []

# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
import random


def non_repeat_num(my_list):
    result_list = []
    for i in range(0, N):
        count = 0
        for k in range(0, N):
            if my_list[i] == my_list[k]:
                count += 1
            if (k == N-1) and (count == 1):
                result_list.append(my_list[i])
    return result_list


N = int(input("Input number: "))
if N <= 0:
    N = int(input("Wrong value of the number of numbers!Input number: "))
list_0 = list(range(N))
list_1 = random.choices(list_0, k=N)
print(list_1)
print(non_repeat_num(list_1))
