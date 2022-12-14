import telebot, random
from telebot import types


likeprofile = []
bot = telebot.TeleBot('5883195717:AAGsI3Jp8Vu79h0ubIg7sZmRUExvalAo9DY')


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


c = random_number()
print(c)


@bot.message_handler(commands=['start'])
def start_message(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton("Чекнуть список")
    btn1000 = types.KeyboardButton("Обратная связь")
    murkup.add(btn1, btn1000)
    bot.send_message(message.chat.id,
                     text="Здравствуйте,{0.first_name}!Вас приветствует телеграмм бот, который может менять школьные звонки посредством голосования.Для корректной работы бота нужно соблюдать несколько правил:    1.Audio файл должен быть от 8-15 секунд     2.Файл не должен содержать мата,резких и режущих звуков."
                          "Для загрузки аудио ,просто отправьте аудио боту".format(message.from_user),reply_markup=murkup)

@bot.message_handler(content_types=['text'])
def obr_sv(message):
    if message.chat.type == 'private':
        if message.text == 'Обратная связь':
            bot.send_message(message.chat.id, 'https://docs.google.com/forms/d/e/1FAIpQLSfnp-w2O2mvRjvA1Y0QBUKO-b1M_tVbtR-CFhk3B2dLcV4YoQ/viewform?usp=sf_link'.format(message.from_user))


@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    global music_number, n
    file_info = bot.get_file(message.audio.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    bot.send_audio('788152184', downloaded_file)
    bot.reply_to(message, 'Аудио добавлено')
    if message.from_user.id == 788152184:
        with open(r"C:\music\music" + str(music_number) + ".mp3", 'wb') as new_file:
            with open('music_number.txt', 'w') as n:
                music_number += 1
                n.write(str(music_number))
            new_file.write(downloaded_file)


@bot.message_handler(content_types=['text'])
def priziv(message):
    global c
    if message.chat.type == 'private':
        if message.text == 'Чекнуть список':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(1, callback_data="bt1")
            markup.add(button1)
            with open('C:\\music\\music' + str(c[0]) + '.mp3', 'rb') as f:
                bot.send_audio(message.chat.id, f)
            bot.send_message(message.chat.id, 'Проголосовать'.format(message.from_user), reply_markup=markup)
            markup = types.InlineKeyboardMarkup()
            button2 = types.InlineKeyboardButton(2, callback_data="bt2")
            markup.add(button2)
            with open('C:\\music\\music' + str(c[1]) + '.mp3', 'rb') as f:
                bot.send_audio(message.chat.id, f)
            bot.send_message(message.chat.id, 'Проголосовать'.format(message.from_user), reply_markup=markup)
            markup = types.InlineKeyboardMarkup()
            button3 = types.InlineKeyboardButton(3, callback_data="bt3")
            markup.add(button3)
            with open('C:\\music\\music' + str(c[2]) + '.mp3', 'rb') as f:
                bot.send_audio(message.chat.id, f)
            bot.send_message(message.chat.id, 'Проголосовать'.format(message.from_user), reply_markup=markup)
            markup = types.InlineKeyboardMarkup()
            button4 = types.InlineKeyboardButton(4, callback_data="bt4")
            markup.add(button4)
            with open('C:\\music\\music' + str(c[3]) + '.mp3', 'rb') as f:
                bot.send_audio(message.chat.id, f)
            bot.send_message(message.chat.id, 'Проголосовать'.format(message.from_user), reply_markup=markup)
            markup = types.InlineKeyboardMarkup()
            button5 = types.InlineKeyboardButton(5, callback_data="bt5")
            markup.add(button5)
            with open('C:\\music\\music' + str(c[4]) + '.mp3', 'rb') as f:
                bot.send_audio(message.chat.id, f)
            bot.send_message(message.chat.id, 'Проголосовать'.format(message.from_user), reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'bt1':
        if likeprofile.count(call.message.from_user.id) == 0:
            likeprofile.append(call.message.from_user.id)
            n = open('like1.txt')
            like = n.readline()
            like = str(int(like) + 1)
            with open('like1.txt', 'w') as n:
                n.write(str(like))
            bot.send_message(call.message.chat.id, 'Лайк засчиан')
        else:
            bot.send_message(call.message.chat.id, 'Ты уже лайкал сегодня')
    if call.data == 'bt2':
        if likeprofile.count(call.message.from_user.id) == 0:
            likeprofile.append(call.message.from_user.id)
            n = open('like2.txt')
            like = n.readline()
            like = str(int(like) + 1)
            with open('like2.txt', 'w') as n:
                n.write(str(like))
            bot.send_message(call.message.chat.id, 'Лайк засчиан')
        else:
            bot.send_message(call.message.chat.id, 'Ты уже лайкал сегодня')
    if call.data == 'bt3':
        if likeprofile.count(call.message.from_user.id) == 0:
            likeprofile.append(call.message.from_user.id)
            n = open('like3.txt')
            like = n.readline()
            like = str(int(like) + 1)
            with open('like3.txt', 'w') as n:
                n.write(str(like))
            bot.send_message(call.message.chat.id, 'Лайк засчиан')
        else:
            bot.send_message(call.message.chat.id, 'Ты уже лайкал сегодня')
    if call.data == 'bt4':
        if likeprofile.count(call.message.from_user.id) == 0:
            likeprofile.append(call.message.from_user.id)
            n = open('like4.txt')
            like = n.readline()
            like = str(int(like) + 1)
            with open('like4.txt', 'w') as n:
                n.write(str(like))
            bot.send_message(call.message.chat.id, 'Лайк засчиан')
        else:
            bot.send_message(call.message.chat.id, 'Ты уже лайкал сегодня')
    if call.data == 'bt5':
        if likeprofile.count(call.message.from_user.id) == 0:
            likeprofile.append(call.message.from_user.id)
            n = open('like5.txt')
            like = n.readline()
            like = str(int(like) + 1)
            with open('like5.txt', 'w') as n:
                n.write(str(like))
            bot.send_message(call.message.chat.id, 'Лайк засчиан')
        else:
            bot.send_message(call.message.chat.id, 'Ты уже лайкал сегодня')


bot.polling(none_stop=True)
