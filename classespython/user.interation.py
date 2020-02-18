from telegram.ext import Updater, CommandHandler
import requests
import re

space_bot_token = "968755596: AAE1HhRPBCgRimj9CjAAvhRSFx45tMoVEGk"
updater = Updater('space_bot_token', use_context=True)



def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))



updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()

# @bot.menssage_handler(commands=["starts", "help"])
# def send_start_message(message):
#     bot.replay_to(message, "Olä sou o bot 'Quem estah no espacö?'\n"
#                   "Envie o comando /people para saber quantas pessoas estäo aqui.")
#
#
# def get_repla_message():
#     pass
#
# @bot.menssage_handler(commands=["people"])
# def send_people(message):
#     bot.replay_to(message, get_repla_message())
#

