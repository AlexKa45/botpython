# -*- coding: utf-8 -*-
import os

import telebot
from flask import Flask, request

TOKEN = '619217456:AAH3t5-puxFnsjg5AzMFpim0zKo-SCKPsMQ'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id,message.text)
        
if "HEROKU" in list(os.environ.keys()):
    server = Flask(__name__)
    
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://0.0.0.0:80") # этот url нужно заменить на url вашего Хероку приложения
        return "?", 200
    
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    bot.remove_webhook()
    bot.polling(none_stop=True)
