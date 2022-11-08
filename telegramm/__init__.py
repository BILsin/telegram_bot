import telebot
from telebot import types
bot = telebot.TeleBot('5727809586:AAG3hCLFivILBnPccENdpuzukdojf-wJW2w')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,text="Здравствуйте, {0.first_name}! Я ваш бот-помогатор для смены школьных звонков".format(message.from_user))
@bot.message_handler(content_types=['text'])
def otvet(message):
    chatID = message.chat.id
    if message.chat.type == "private":
        if message.text == 'Привет бот':
            bot.send_message(message.chat.id,text="Ты кого ботярой назвал падла.Быканул?".format(message.from_user))
        else:
            bot.send_message(message.chat.id, text="Ничего не понял пиши разборчивее".format(message.from_user))
bot.polling(none_stop = True)

