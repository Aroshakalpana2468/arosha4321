import os
import telebot

bot = telebot.TeleBot("5258585368:AAEMvwmIs1-dsfwyUcow9AmP0X2Dx31vMeM")


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
  bot.send_message(message,"sorry danne na")

bot.polling()






