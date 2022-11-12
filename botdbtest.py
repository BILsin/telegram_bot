import telebot, time, schedule, sqlite3


bot = telebot.TeleBot('5729622786:AAHSoj7aXoRVQGQQ8dLK__66beyZfPUHHCE')
conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INT PRIMARY KEY,
            user_name TEXT );
""")
conn.commit()


def db_table_val(user_id: int, user_name: str):
    cur.execute('INSERT INTO test (user_id, user_name) VALUES (?, ?)', (user_id, user_name))
    conn.commit()


@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text.lower() == '/start':
        bot.send_message(message.from_user, 'Ну привет, красавчик. Хочешь что бы я добавил тебя в свою базу данных? Тогда напиши мне "/add"')


@bot.message_handler(content_types=['text'])
def users_add(message):
    if message.text.lower() == '/add':
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        db_table_val(user_id=us_id, user_name=us_name)
        bot.send_message(message.chat.id, 'Ты в моей базе данных-_-')


def musicdb_add(user_id: int, user_name: str):
    cur.execute('INSERT INTO users(?, ?); VALUES (?, ?)')
    conn.commit()


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


def send_message():
    bot.send_message('788152184', 'время кушац') #Тут потом будет нормальная рассылка, это просто сообщение для проверки функционала


schedule.every().day.at("23:42").do(send_message)


while True:
    schedule.run_pending()
    time.sleep(1)


bot.polling(none_stop=True)
