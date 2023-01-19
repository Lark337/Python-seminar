# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные данные хранятся в отдельных текстовых файлах.
data = open('5/data.txt','r')
text = data.read()
data.close()
def compression(text):
    i = text.index('"')
    list1 = list(text[i + 1:len(text) - 1])
    stroka = str()
    count = 0
    for i in range (len(list1) - 1):
        count += 1
        if list1[i] != list1[i+1]:
            stroka += f'{count}{list1[i]}'
            count = 0
    else:
        stroka += f'{count + 1}{list1[i+1]}'
    res = text[:10] + stroka + '"'
    return res

def decompression(text):
    i = text.index('"')
    stroka1 = text[i + 1:len(text) - 1]
    stroka2 = str()
    for i in range (len(stroka1) - 1):
        if stroka1[i].isdigit():
            stroka2 += int(stroka1[i]) * stroka1[i+1]
    res = text[:10] + stroka2 + '"'
    return(res)

print('Ввод:',text)
for i in range (len(text)):
    if text[i].isdigit():
        print(f'Вывод: {decompression(text)}')
        break
else:
    print(f'Вывод: {compression(text)}')