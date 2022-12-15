# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099
from math import *
x1 = float(input("Input x1 = "))
y1 = float(input("Input y1 = "))
x2 = float(input("Input x2 = "))
y2 = float(input("Input y2 = "))

d = round(sqrt(((x2-x1)**2)+((y2-y1)**2)), 3)
print(d)
