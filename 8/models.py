def init():
    data = open('8/data.txt','r', encoding='UTF8')
    text = data.readlines()
    print(data.read())
    data.close
    return text

def add(text):
    predmet = input('Введите предмет: ') + '\n'
    predmet_index = text.index(predmet)
    name = input('Введите имя: ')
    for i in range(predmet_index,len(text)):
        stroka = text[i]
        if name in stroka:
            text[i].split('\n')
            find = text[i]
            check = 1
            break
    else:
        check = 0
        print('Такого ученика нет')
    if check == 1:
        print (find)
        find = find.strip()
        dobavit = input('Введите оценки через пробел: ')
        find += ' ' + dobavit +'\n'
        text[i] = find
        text = ''.join(text)
        print(text)
        with open('8/data.txt','w', encoding='UTF8') as data:
    	    data.write(text)

def show(text):
    name = input('Введите имя: ')
    list1 = ['Информатика\n','Математика\n','Русский язык\n']
    for i in range(len(text)):
        if text[i] in list1:
            for j in range(i,len(text)):
                stroka = text[j]
                if name in stroka:
                    stroka = stroka.split()
                    list2 = ' '.join(stroka[2:])
                    print(f'{text[i]}{list2}\n')
                    break
    else:
        print('Такого ученика нет')