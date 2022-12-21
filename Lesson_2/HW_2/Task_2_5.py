# 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randrange, randint

N = int(input("Input number: "))

new_list = list(range(N))
print(new_list)

for i in range(N):
    num_1 = randint(0, N-1)
    num_2 = randint(0, N-1)
    new_list[num_1], new_list[num_2] = new_list[num_2], new_list[num_1]

print(new_list)
