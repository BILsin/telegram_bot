import telebot, time, schedule, sqlite3, random, types
from telebot import types


bot = telebot.TeleBot('5729622786:AAHSoj7aXoRVQGQQ8dLK__66beyZfPUHHCE')


@bot.message_handler(commands=['start'])
def start_message(message):
    murkup =types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton("Чекнуть список")
    murkup.add(btn1)
    bot.send_message(message.chat.id,text = "hi".format(message.from_user), reply_markup=murkup)


@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    try:
        file_info = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'C:/' + file_info.file_path
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.reply_to(message, "Аудио добавлено")
    except Exception as e:
        bot.reply_to(message, e)


def random_number():
    k = 0
    c = []
    while k != 5:
        if k == 5:
            break
        n = open('music_number.txt')
        X = random.randrange(0, int(n.readline()))
        if c.count(X) == 0:
            c.append(X)
        elif len(c) == 5:
            break
        else:
            continue
    return c
@bot.message_handler(content_types=['text'])
def priziv(message):
    if message.chat.type == 'private':
        if message.text == 'Чекнуть список':
            c = random_number()
            print(c)
            murkup = types.InlineKeyboardMarkup()
            for i in range(0, 5):
                n = c[i]
                btn = types.InlineKeyboardButton(str(n), cllback_data="test")
                murkup.add(btn)
                with open('C:\\music\\music' + str(n) + '.mp3', 'rb') as f:
                    bot.send_audio(message.chat.id, f)
                bot.send_message(message.chat.id, 'Поставить лайк'.format(message.from_user), reply_markup=murkup)





bot.polling(none_stop=True)
