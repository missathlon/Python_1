# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample


def num_result(a):
    new_list = sample(range(1, a*5), k=a)
    print(new_list)
    result_list = []
    if a % 2 == 0:
        k = int(a/2)
        for i in range(0, k):
            result_list.append(new_list[i]*new_list[a-1-i])
        print(result_list)
    else:
        k = int((a-1)/2)
        for i in range(0, k):
            result_list.append(new_list[i]*new_list[a-1-i])
        result_list.append(new_list[k])
        print(result_list)


a = int(input("Input number: "))
num_result(a)
