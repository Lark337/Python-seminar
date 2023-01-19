# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.


import random
def hard():
    left = 120
    check = 115
    while left > 0:
        num = int(input('Введите число конфет '))
        while num > 28 or num < 1:
            print('Введенное число должно быть между 1 и 28')
            num = int(input('Введите число конфет '))
        left -= num
        if left <= 0:
            print('Вы победили')
            break
        if left < check:
            check -= 29
        bot = left - (check + 1)
        if bot <= 0:
            bot = random.randint(1,28)
        if left <= 28:
            print(f'Бот взял {left} \nВы проиграли')
            break
        left -= bot
        print(f'Бот взял {bot}, осталось {left}')

def easy():
    left = 120
    while left > 0:
        num = int(input('Введите число конфет '))
        while num > 28 or num < 1:
            print('Введенное число должно быть между 1 и 28')
            num = int(input('Введите число конфет '))
        left -= num
        if left <= 0:
            print('Вы победили')
            break
        if left <= 28:
            print(f'Бот взял {left} \nВы проиграли')
            break
        bot = random.randint(1,28)
        left -= bot
        print(f'Бот взял {bot}, осталось {left}')

difficulty = int(input('Выберите сложность 1 или 2: '))
if difficulty == 1:
    easy()
elif difficulty == 2:
    hard()
 


