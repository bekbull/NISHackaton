#!/usr/bin/env python3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import constants
import time
from datetime import datetime
import sql_queries as sql

updater = Updater(token=constants.toqen)
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hey I was created by r1chter1.')

def textMessage(bot, update):
    response = 'MAL'
    bot.send_message(chat_id=update.message.chat_id, text=response)

def individualreq(bot, update, args):
    args[-1] = args[-1].upper()
    w = ''.join(args)
    text = update.message.text
    text = text[1:]
    
    if datetime.today().weekday() == 0:
        res = sql.monday(w)
        print(res)
        for lesson in res[0]:
            bot.send_message(chat_id=update.message.chat_id, text=lesson)

    elif datetime.today().weekday() == 1:
        res = sql.tuesday(w)
        print(res)
        for lesson in res[1]:
            bot.send_message(chat_id=update.message.chat_id, text=lesson)

    elif datetime.today().weekday() == 2:
        res = sql.wednesday(w)
        print(res)
        for lesson in res[0]:
            bot.send_message(chat_id=update.message.chat_id, text=lesson)

    elif datetime.today().weekday() == 3:
        res = sql.thursday(w)
        print(res)
        for lesson in res[0]:
            bot.send_message(chat_id=update.message.chat_id, text=lesson)

    elif datetime.today().weekday() == 4:
        res = sql.friday(w)
        print(res)
        for lesson in res[0]:
            bot.send_message(chat_id=update.message.chat_id, text=lesson)

    elif datetime.today().weekday() == 5 or datetime.today().weekday() == 6:
        print(*args)
        bot.send_message(chat_id=update.message.chat_id, text="Weekend...")
    else:
        bot.send_message(chat_if=update.message.chat_id, text="Something wrong...")

start_command_handler = CommandHandler(['start'], startCommand, pass_args=False)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(CommandHandler(['timetable'], individualreq, pass_args=True))

updater.start_polling(clean=True)

updater.idle()