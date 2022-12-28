# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

import random
b = str
k = int(input('Введите натуральную степень: '))
while k > 1:
    a = random.randint(0, 100)
    print(f'{a}x^{k}', end = ' + ')
    k -= 1
if k > 0:
    a = random.randint(0, 100)
    print(f'{a}x', end = ' ')
a = random.randint(0, 100)
print(f'+ {a}', end = '')