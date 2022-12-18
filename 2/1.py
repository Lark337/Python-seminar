# 1) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

list = []
n = int(input('Введите число '))
res = 1
for i in range (1, n+1):
    res *= i
    list.append(res)
print(list)