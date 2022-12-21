# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

from decimal import Decimal

number = input("Input number: ")
len_number = len(number)
number_1 = float(number)
a = Decimal(number_1*(10**(len_number-2)))

sum = 0
while a >= 1:
    sum += a % 10
    a = a//10
print(sum)
