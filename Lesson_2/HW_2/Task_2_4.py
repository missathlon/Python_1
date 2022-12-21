#  4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

N = int(input("Enter the value of N: "))

new_list = []

for i in range(0, 2*N+1):
    a = (-N)+i
    new_list.append(a)
print(new_list)

a = len(new_list)
print(a)
num_1 = int(input("Position one: "))
while num_1 < 1 or num_1 > a:
    num_1 = int(input("Try again: "))
num_2 = int(input("Position two: "))
while num_2 < 1 or num_2 > a:
    num_2 = int(input("Try again: "))
result = new_list[num_1-1]*new_list[num_2-1]
print(result)
