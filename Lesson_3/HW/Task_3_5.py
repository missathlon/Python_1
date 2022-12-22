# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def NegaFibonacci(n):
    list_1 = []
    a = 0
    list_1.insert(0, 0)
    list_1.insert(1, 1)
    list_1.insert(0, 1)
    k = 0
    for i in range(3, 2*n, 2):
        a = list_1[i-2]+list_1[i-1]
        list_1.append(a)
        m = ((-1)**(k+1))*a
        list_1.insert(0, m)
        k += 1
    return list_1


n = int(input("Input number: "))
print(NegaFibonacci(n))
