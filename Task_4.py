# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

q = int(input("Input quarter = "))

if q == 1:
    print("x > 0 and y > 0")
elif q == 2:
    print("y > 0 and x < 0")
elif q == 3:
    print("y < 0 and x < 0")
elif q == 4:
    print("y < 0 and x > 0")
else:
    print("This quarter doesn`s exist")
