print("Бот запущен")
import telebot
import pyTelegramBotAPI

TOKEN = '6128827941:AAHpEN5qv7ZONScO5JWnsft2nl12lt9fUAM'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
 if message.text == "/start":
     bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
 elif message.text == "/help":
    bot.send_message(message.from_user.id, "Вот команды которе есть в боте /pay /help /start /zoom")
 elif message.text == "/pay":
     bot.send_message(message.from_user.id, "Это команда пока в разроботке")
 elif message.text == "/zoom":
     bot.send_message(message.from_user.id, "Вот сылка на урок Zoom: ")
 else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling()
