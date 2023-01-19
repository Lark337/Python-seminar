# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.
list1 = ['1', '2', '3' , '4' , '5', '6' ,'7' , '8' , '9']
switch = 0
print(list1)
def pole():
    print(f'{list1[0]}|{list1[1]}|{list1[2]}|')
    print(f'{list1[3]}|{list1[4]}|{list1[5]}|')
    print(f'{list1[6]}|{list1[7]}|{list1[8]}|')
pole()
def Current(n):
    switch = 0
    while switch == 0:
        curr = int(input(f'{n} игрок: '))
        if list1[curr - 1] != 'X' and list1[curr - 1] != 'O':
            switch = 1
        else:
            print('Клетка уже занята')
    if n == 1:
        list1[curr - 1] = 'X'
    else: 
        list1[curr - 1] = 'O'

def check(list1):
    return (list1[0] == list1[1] == list1[2] 
    or list1[3] == list1[4] == list1[5] 
    or list1[6] == list1[7] == list1[8] 
    or list1[0] == list1[3] == list1[6]
    or list1[1] == list1[4] == list1[7]
    or list1[2] == list1[5] == list1[8]
    or list1[0] == list1[4] == list1[8]
    or list1[2] == list1[4] == list1[6])
count = 0
while count != 9:
    Current(1)
    count += 1
    pole()
    if check(list1):
        print('Победил первый игрок')
        break
    if count == 9:
        print('Ничья')
        break
    Current(2)
    count += 1
    pole()
    if check(list1):
        print('Победил второй игрок')
        break
    print(count)

