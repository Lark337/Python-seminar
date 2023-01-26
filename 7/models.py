def add():
    check = False
    while check == False:
        data1 = open('7/data1.txt','a')
        lastName = input('Введите фамилию: ')
        firstName = input('Введите имя: ')
        phoneNumber = input('Введите телефон: ')
        info = input('Введите дополнительную информацию: ')
        data1.write(f'{lastName}\n{firstName}\n{phoneNumber}\n{info}\n')
        data1.write('-----------------\n')
        data2 = open('7/data2.txt','a')
        data2.write(f'{lastName},{firstName},{phoneNumber},{info}\n')
        if int(input('Добавить ещё контакт?\n1 - да\n2 - нет\n')) == 2:
            check = True
    data1.close
    data2.close

def show():
    a = int(input('В каком формате отобразить?\n1 - Столбец\n2 - Строка\n'))
    if a == 1:
        data1 = open('7/data1.txt','r')
        text = data1.read()
        print(text)
        data1.close
    if a == 2:
        data2 = open('7/data2.txt','r')
        text = data2.read()
        print(text)
        data2.close