# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
list1 = [1, 0, 1]
a = 0
b = 1
count = int(input('Сколько чисел Фибоначчи: '))
if count == 0:
    print('0')
    exit()
for i in range(2, count + 1):
    c = a + b
    a = b
    b = c
    list1.append(c)
    if i % 2 > 0:
        list1.insert(0, c)
    else:
        list1.insert(0, -c)
print(list1)
    