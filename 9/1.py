# 1) Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)
# Пример:
# привет приабвет ограбпв
# Ответ:
# привет ограбпв

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

token1 = '5952319972:AAExryZaCoLuiqm6vl0x-xdx0dnTcVcsG0E'
bot = Bot(token1)

updater =Updater(token1)
dispatcher = updater.dispatcher

def delete(update, context):
    stroka = update.message.text
    stroka = stroka.split()
    list1 = [i for i in stroka if 'абв' not in i.lower()]
    context.bot.send_message(update.effective_chat.id, ' '.join(list1))

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите слова через пробел из которых нужно удалить 'абв': ")

start_handler = CommandHandler('start', start)
delete_handler = MessageHandler(Filters.text, delete)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(delete_handler)

updater.start_polling()
updater.idle()