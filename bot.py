#!/usr/bin/env python3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import constants
import time
from datetime import datetime
import sql_queries as sql

updater = Updater(token=constants.toqen)
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hey, it is Robobot C 1.1.')

def textMessage(bot, update):
    response = 'I copy your message, as you copy other answers at СОР: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)

def individualreq(bot, update, args):
    text = update.message.text
    text = text[1:]
    command = ''
    for c in text:
        if c == ' ':
            break
        command += c
    print(text,command)
    print(datetime.today().weekday())
    if datetime.today().weekday() == 1:
        print('YESS')
        print(args[0])
        res = sql.monday(args[0])
        print(res)
        for lesson in res[0]:
            bot.send_message(chat_id=update.message.chat_id, text=lesson)

start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(CommandHandler(['timetable', 'help', 'admin', 'suggest'], individualreq, pass_args=True))

updater.start_polling(clean=True)

updater.idle()
