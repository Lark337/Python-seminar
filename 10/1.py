from telegram import Bot, User
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from time import asctime

token1 = ''
bot = Bot(token1)

updater =Updater(token1)
dispatcher = updater.dispatcher

def calcul(update, context):
    primer = update.message.text
    ''.join(primer.strip())
    first_i = 0
    list1 = []
    for i in range(len(primer)):
        if primer[i] == '+' or primer[i] == '-' or primer[i] == '/' or primer[i] == '*':
            list1.append(primer[first_i:i])
            list1.append(primer[i])
            first_i = i+1
    else:
        list1.append(primer[first_i:len(primer)])
    
    while '*' in list1 or '/' in list1:
        for j in list1:
            if j == '*':
                i = list1.index(j)
                temp = float(list1[i-1]) * float(list1[i+1])
                del list1[i:i+2]
                list1[i-1] = temp
                break
            elif j == '/':
                i = list1.index(j)
                temp = float(list1[i-1]) / float(list1[i+1])
                del list1[i:i+2]
                list1[i-1] = temp
                break
    
    
    while '+' in list1 or '-' in list1:
        for j in list1:
            if j == '-':
                i = list1.index(j)
                temp = float(list1[i-1]) - float(list1[i+1])
                del list1[i:i+2]
                list1[i-1] = temp
                break
            elif j == '+':
                i = list1.index(j)
                temp = float(list1[i-1]) + float(list1[i+1])
                del list1[i:i+2]
                list1[i-1] = temp
                break
    res = list1[0]
    context.bot.send_message(update.effective_chat.id, res)
    log(update,primer,res)       

def log(update,primer,res):
    id = update.effective_chat.id
    time = asctime()
    name = update.effective_chat.first_name
    stroka = f'{time} id {id} Имя {name} Ввод {primer} Результат {res}\n'
    with open('10/log.txt','a', encoding='UTF8') as data:
    	    data.write(stroka) 

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите пример: ")


start_handler = CommandHandler('start', start)
delete_handler = MessageHandler(Filters.text, calcul)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(delete_handler)

updater.start_polling()
updater.idle()