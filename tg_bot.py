# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# updater = Updater(token='2095253159:AAGEhnDpruN1ML4gfQ9IOf5P2seOyl_dROA') # Токен API к Telegram
# disp = updater.dispatcher
# def start_mes(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text='hi bro')
# start_handler=CommandHandler('start', start_mes)
# disp.add_handler(start_handler)
# updater.start_polling()
# updater.idle()

import telebot
import datetime

bot = telebot.TeleBot('2095253159:AAGEhnDpruN1ML4gfQ9IOf5P2seOyl_dROA')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, давай начинать!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'И тебе привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'И тебе пока!')
    elif message.text.lower() == 'дата':
        bot.send_message(message.chat.id, datetime.datetime.today().strftime('%d.%m.%Y'))
    elif message.text.lower() == 'время':
        bot.send_message(message.chat.id, datetime.datetime.today().strftime('%H:%M:%S'))
    elif message.text.lower() == 'день недели':
        bot.send_message(message.chat.id, datetime.datetime.today().strftime('%A'))


bot.polling()