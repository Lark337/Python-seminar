# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('Введите число: '))
res = ''
if num == 0:
    print(0)
    exit()
while num > 0 :
    a = num % 2
    res = str(a) + res
    num = num // 2
print(res)
