# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
n = abs(int(input('Введите число ')))
array = []
for i in range (-n, n + 1):
    array.append(i)
indList = list(map (int, input('Введите список индексов через пробел ').split()))
res = 1
for i in range(len(indList)):
    res *= array[indList[i]]
print(array)
print(indList)
print(res)