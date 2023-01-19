#  4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0
import random


def create_str(n, list_0):

    with open("str_1.txt", "a", encoding="utf-8") as file:
        k = 0
        for i in range(n, 0, -1):
            coef = random.choice(list_0)

            if coef == 0:
                file.write("")
                k += 1
            else:
                file.write(f"{coef}*x^{(n-k)} + ")
                k += 1

        file.write(f"{coef} = 0\n")


k = int(input("Введите натуральную степень k = "))

list_0 = list(range(0, 10))

create_str(k, list_0)

# from random import choice, sample


# def polynomial(num: int):
#     if num < 1:
#         return 0

#     poly = ""
#     num_list = range(0, 11)

#     with open("poly_2.txt", "a", encoding="utf-8") as my_f:
#         for i in range(num, 1, -1):
#             value = choice(num_list)
#             if value:
#                 poly += f"{value}*x^{i} {choice('+-')} "

#         numbers = sample(range(1, 11), k=2)
#         my_f.write(f"{poly}{choice(numbers)}*x {choice('+-')} {choice(numbers)} = 0\n")


# for _ in range(3):
#     polynomial(int(input()))
