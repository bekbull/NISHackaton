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
    response = '/timetable' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)

def individualreq(bot, update, args):
    args = args.split
    args[-1] = args[-1].upper()
    text = update.message.text
    text = text[1:]
    command = ''
    for c in text:
        if c == ' ':
            break
        command += c
    print(command, text)
    print(datetime.today().weekday() + 1)

    if datetime.today().weekday() == 0:
        print('YESS, It is Monday, man.')
        print(args[0])
        res = sql.monday(args[0])
        print(res)
        for lesson in res[0]:
            bot.send_message(chat_id=update.message.chat_id, text=lesson)

    elif datetime.today().weekday() == 1:
        print('YESS, It is Tuesday, man.')
        print(args[0])
        res = sql.tuesday(args[0])
        print(res)
        for lesson in res[1]:
            bot.send_message(chat_id=update.message.chat_id, text=lesson)
        #bot.send_message(chat_id=update.message.chat_id, tex='YESS, It is Tuesday, man.')

    elif datetime.today().weekday() == 2:
        print('YESS, It is Wednesday, man.')
        print(args[0])
        res = sql.wednesday(args[0])
        print(res)
        for lesson in res[0]:
            bot.send_message(chat_id=update.message.chat_id, text=lesson)

    elif datetime.today().weekday() == 3:
        print('YESS, It is Thursday, man.')
        print(args[0])
        res = sql.thursday(args[0])
        print(res)
        for lesson in res[0]:
            bot.send_message(chat_id=update.message.chat_id, text=lesson)

    elif datetime.today().weekday() == 4:
        print('YESS, It is Friday, man.')
        print(args[0])
        res = sql.friday(args[0])
        print(res)
        for lesson in res[0]:
            bot.send_message(chat_id=update.message.chat_id, text=lesson)

    elif datetime.today().weekday() == 5:
        bot.send_message(chat_id=update.message.chat_id, text="Weekend...")

    elif datetime.today().weekday() == 6:
        bot.send_message(chat_id=update.message.chat_id, text="Weekend...")
    else:
        bot.send_message(chat_if=update.message.chat_id, text="Something wrong...")

start_command_handler = CommandHandler('Click this Click.', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(CommandHandler(['timetable', 'help', 'admin', 'suggest'], individualreq, pass_args=True))

updater.start_polling(clean=True)

updater.idle()
