# -*- coding: utf-8 -*-
import os

import telebot
from flask import Flask, request

TOKEN = '619217456:AAH3t5-puxFnsjg5AzMFpim0zKo-SCKPsMQ'
bot = telebot.TeleBot(TOKEN)

def main():
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id,message.text)
    

if __name__ == "__main__":
    main()
    bot.set_webhook(url='https://demo45.herokuapp.com/')
