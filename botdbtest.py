import telebot, time, schedule, sqlite3, random, types
from telebot import types


c = list()
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
    global c
    n = open('music_number.txt')
    X = random.randrange(0, int(n.readline()))
    if c.count(X) == 0:
        return X


def send_message():
    global c
    k = 0
    while k != 5:
        x = random_number()
        if c.count(x) == 0 and x != 'none' and x != 'None' and x != 'NONE':
            c.append(random_number())
            k += 1
        if k == 5: break
        else: continue
    print(c)
    for i in range(0, 5):
        n = c[i]
        file_inf = open('C:\\music\\music' + str(n) + '.mp3', 'rb')
        bot.send_audio('788152184', file_inf)


schedule.every().day.at("08:56").do(send_message)


while True:
    schedule.run_pending()
    time.sleep(1)


bot.polling(none_stop=True)
