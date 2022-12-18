# 4)Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.
n = int(input('Введите число '))
list = []
for i in range(n+1):
    list.append(i)
res = 0
for i in range (0, len(list),2):
    res += list[i]
    print(res)
print(list)
print(res)