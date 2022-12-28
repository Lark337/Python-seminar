# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list1 = list(map(int,input('Введите числа через пробел: ').split()))
list2 = []
print(list1)
while len(list1) > 0:
    i = list1[0]
    list1.remove(i)
    if i in list1:
        while i in list1:
            list1.remove(i)
    else:
        list2.append(i)
print(list2)