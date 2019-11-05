#!/usr/bin/env python3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import constants
import time
from datetime import datetime
import sql_queries as sql
import logging
from time import sleep

updater = Updater(token=constants.toqen)
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hey I was created by r1chter1.')
    help_bot(bot, update)

def textMessage(bot, update):
    response = 'MAL'
    bot.send_message(chat_id=update.message.chat_id, text=response)

logger = logging.getLogger()

def draft(bot, update):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],
                [InlineKeyboardButton("Option 3", callback_data='3'),
                InlineKeyboardButton("NIS-web", url='https://i0bster.github.io/nis-web/')]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def help_bot(bot, update):
    response = ['/timetable "class"', '/help - to see commands', '/del - to clear chat']
    for i in response:
        bot.send_message(chat_id=update.message.chat_id, text=i)
    

def delete_msg(bot, update):
    print(update.message.message_id, type(update.message.message_id))
    bot.send_message(chat_id=update.message.chat_id, text='Cleaning in process...')
    lastid = update.message.message_id + 1
    print('qq', lastid, type(lastid))
    sleep(2)
    for i in range(1000):
        msgid = update.message.message_id - i
        bot.deleteMessage(chat_id=update.message.chat_id, message_id=msgid)    
    bot.deleteMessage(chat_id=update.message.chat_id, message_id=lastid)




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
        for lesson in res[0]:
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
draft = CommandHandler(['draft'], draft, pass_args=False)
help_bot_handler = CommandHandler(['help'], help_bot, pass_args=False)
delete_bot_handler =CommandHandler(['del'], delete_msg, pass_args=False)

dispatcher.add_handler(help_bot_handler)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(draft)
dispatcher.add_handler(delete_bot_handler)
dispatcher.add_handler(CommandHandler(['timetable'], individualreq, pass_args=True))

updater.start_polling(clean=True)

updater.idle()