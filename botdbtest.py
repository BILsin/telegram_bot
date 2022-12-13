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


def send_message():
    c = random_number()
    print(c)
    for i in range(0, 5):
        n = c[i]
        murkup =  types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton()
        file_inf = open('C:\\music\\music' + str(n) + '.mp3', 'rb')
        bot.send_audio('788152184', file_inf)


schedule.every().day.at("09:13").do(send_message)


while True:
    schedule.run_pending()
    time.sleep(1)


bot.polling(none_stop=True)
