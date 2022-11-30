import telebot, time, schedule, sqlite3, random, types
from telebot import types


bot = telebot.TeleBot('5729622786:AAHSoj7aXoRVQGQQ8dLK__66beyZfPUHHCE')


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


def f():
    a = []
    n = open('music_number.txt')
    for i in range(0, 5):
        X = random.randrange(0, int(n.readline())-1)
        if a.count(X) == 0:
            a.append(X)
            return a
        print(a)


def send_message():
    c = f()
    for i in range(0, 4):
        file_inf = open('C:\\music\\music' + str(c[i]) + '.mp3', 'rb')
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_audio('788152184', file_inf, reply_markup=murkup)
        btn = types.KeyboardButton('music' + str(c[i]))
        murkup.add(btn)


schedule.every().day.at("12:23").do(send_message)


while True:
    schedule.run_pending()
    time.sleep(1)


bot.polling(none_stop=True)
