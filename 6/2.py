# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

list1 = [2, 33, 'asdas', 3, 'fdsfs',5]
list2 = list(filter(lambda x: type(x) == str,list1))
list3 = list(filter(lambda x: type(x) == int,list1))
print(list1)
print(list2, list3)