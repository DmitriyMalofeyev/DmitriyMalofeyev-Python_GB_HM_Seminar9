from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint as rd

bot = Bot(token=' ')
updater = Updater(token='')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Hi, man')


def rand(update, context):
    context.bot.send_message(update.effective_chat.id, f'{rd(1, 100)}')


def wiki(update, context):
    text = ' '.join(context.args)


def voice(update, context):
    text = update.message.text
    if 'прив' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'И тебе привет, мой дорогой друг!')
    else:
        context.bot.send_message(update.effective_chat.id, 'Я тебя не понимаю :(')


def delete_abc(update, context):
    context.bot.send_message(update.effective_chat.id, 'Удаляю слова с "а", "б", "в" ')
    words = context.args
    words = [word for word in words if not "а" in word]
    words = [word for word in words if not "б" in word]
    words = [word for word in words if not "в" in word]
    answer = " ".join(words)
    context.bot.send_message(update.effective_chat.id, f'Удалено.\n"{answer}"')


start_handler = CommandHandler('start', start)
random_handler = CommandHandler('random', rand)
del_handler = CommandHandler('del', delete_abc)
message_handler = MessageHandler(Filters.text, voice)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_handler)
dispatcher.add_handler(del_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
