# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list1 = list(map(int,input('Введите числа через пробел: ').split()))
list2 = []
res = 0
i = 0
while i < len(list1) / 2:
    res = list1[i] * list1[len(list1)-1-i]
    list2.append(res)
    i += 1
print(list2)