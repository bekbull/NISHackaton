from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from constants import constants
import time

updater = Updater(token=constants.toqen)
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hey, it is Robobot C 1.1.')

def textMessage(bot, update):
    response = 'I copy your message, as you copy other answers at СОР: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)



start_command_handler = CommandHandler('start', startCommand)

text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)

dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()
