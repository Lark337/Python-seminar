# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random
list1 = []
list2 = []
for i in range(0, int(input('Введите размер листа: '))):
    a = round(random.random() * 10, 2)
    list1.append(a)
print(list1)
for i in range(0, len(list1)):
    res = round(list1[i] - int(list1[i]),2)
    list2.append(res)
res = round(max(list2) - min(list2), 2)
print(res)