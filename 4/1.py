# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ round())

import math
a = str(math.pi)
n = int(input('Введите колличство знаков после запятой: '))
a = a[:2+n]
a = float(a)
print(a)