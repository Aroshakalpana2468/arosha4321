import os
import telebot

bot = telebot.TeleBot("API Key here")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Arosha Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/aastrem")

@bot.message_handler(commands=["hi"])
def send_message(message):
  bot.send_message(message,"HI how are you")

@bot.message_handler(commands=["help"])
def send_message(message):
  bot.send_message(message.chat.id,"what is your prashnaya")

@bot.message_handler(commands=["id"])
def send_message(message):
  bot.reply_to(message.chat.id)

bot.polling()






