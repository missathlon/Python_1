# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011


def print_list(n):
    n_list = []
    while n:
        n_list.append(n % 2)
        n //= 2

    return n_list


n = int(input("Input number: "))

new_list = print_list(n)

new_list.reverse()

print(new_list)
