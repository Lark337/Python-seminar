# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))
list = []
i = 2
while n != 1:
    if n % i == 0:
        list.append(i)
        n /= i
        i = 2
    else:
        i += 1
print(list[0], end = ' ')
for i in range(1,len(list)):
    print(f'* {list[i]}', end = ' ')