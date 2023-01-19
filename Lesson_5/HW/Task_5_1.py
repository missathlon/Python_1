# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample


def make_list(number: int, letters='абв'):
    list_0 = []
    for i in range(number):
        set = sample(letters, 3)
        list_0.append("".join(set))
    print(" ".join(list_0))
    return list_0


def filter_words(some_list):
    res_list = []
    for i in some_list:
        if i != "абв":
            res_list.append(i)
    return " ".join(res_list)


num = int(input("Number of words: "))
while num <= 0:
    num = int(input("The data is incorrect. Number of words: "))
    
list_1 = make_list(num)
print(filter_words(list_1))
