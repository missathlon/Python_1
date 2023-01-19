#  5. Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match!

line_count = sum(1 for line in open('str.txt'))
line_count_1 = sum(1 for line in open('str.txt'))
if line_count != line_count_1:
    print("The contents of the files do not match!")

with open("str_res.txt", "w", encoding="utf-8") as file:
    for i in range(0, line_count):
        st1 = open('str.txt').read().split('\n')[i]
        str1 = str(st1)
        st_1_len = len(str1)
        st2 = open('str_1.txt').read().split('\n')[i]
        str2 = str(st2)
        file.write(f"{str1[0:st_1_len-4]} + {str2}\n")


# from random import choice


# def poly_sum(name_1: str, name_2: str):
#     with open(name_1, "r", encoding="utf-8") as my_f_1, \
#             open(name_2, "r", encoding="utf-8") as my_f_2:
#         first = my_f_1.readlines()
#         second = my_f_2.readlines()

#         if len(first) == len(second):
#             with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
#                 for i, v in enumerate(first):
#                     my_f_3.write(f"{v[:-5]} + {second[i]}")
#         else:
#             print("The contents of the files do not match!")


# # poly_sum(input("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
# poly_sum("poly.txt", "poly_2.txt")
