import telebot, sqlite3


n = open('music_number.txt')
music_number = int(n.readline())
bot = telebot.TeleBot('5729622786:AAHSoj7aXoRVQGQQ8dLK__66beyZfPUHHCE')
conn = sqlite3.connect('users.db', check_same_thread=False)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INT PRIMARY KEY,
            username TEXT );
""")
conn.commit()
conn2 = sqlite3.connect('music.db', check_same_thread=False)
cur2 = conn.cursor()
cur2.execute("""CREATE TABLE IF NOT EXISTS music(
            music_id INT PRIMARY KEY,
            music_name TEXT,
            music_hash TEXT,
            music_mod INT,
            music_leader_vote INT );
""") #создаёт столбики в базе данных
conn2.commit() #возвращает курсор в нач. положение


def music_db_mod(music_id: int, music_name: str, music_hash: str, music_mod: int, music_leader_vote: int):
    cur2.execute('INSERT INTO music (music_id, music_name, music_hash, music_mod, music_leader_vote) VALUES(?, ?, ?, ?, ?', (music_id, music_name, music_hash, music_mod, music_leader_vote))
    conn2.commit()


def users_db_add(user_id: int, username: str):
    cur.execute('INSERT INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message, res=False):
    bot.send_message(message.from_user.id, 'Ну привет, красавчик. Ты в моей базе данных:_)')
    us_id = message.from_user.id
    us_name = message.from_user.username
    users_db_add(user_id=us_id, username=us_name)


@bot.message_handler(content_types=['text'])
def vnsdb(message):
    if message == 'привет':
        bot.send_message(message.from_user.id, 'РНПВГНРГВРПЫ')


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


bot.polling(none_stop=True)
