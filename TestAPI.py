# -*- coding: utf-8 -*-
import config
import telebot
import requests
from telebot import types

data ={'name':'Name',
       'num':0}

bot = telebot.TeleBot(config.token)
#markup = types.ReplyKeyboardMarkup()

def enter():
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, config.text)
        bot.send_message(message.chat.id, "Введите ФИО ")
    
    @bot.message_handler(regexp="[-+]?\d+")
    def number(message):
        data['num'] = message.text
        sign_up()

    @bot.message_handler(content_types=['text'])
    def fio(message):
        data['name'] = message.text
        bot.send_message(message.chat.id,"Введите номер по договору")
        
        
def sign_up():
    print('\n',data['num'],'\n',data['name'])
    requests.get(config.url + )

if __name__ == '__main__':
     enter()
     bot.polling(none_stop=True)
