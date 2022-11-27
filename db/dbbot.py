import telebot, sqlite3


bot = telebot.TeleBot('5729622786:AAHSoj7aXoRVQGQQ8dLK__66beyZfPUHHCE')
conn = sqlite3.connect('users.db', check_same_thread=False)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INT PRIMARY KEY,
            user_name TEXT );
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


def users_db_add(user_id: int, user_name: str):
    cur.execute('INSERT INTO users (user_id, user_name) VALUES (?, ?)', (user_id, user_name))
    conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message, res=False):
        bot.send_message(message.from_user.id, 'Ну привет, красавчик. Хочешь что бы я добавил тебя в свою базу данных? Тогда напиши мне "/add"')


@bot.message_handler(commands=['add'])
def users_add(message, res=False):
        bot.send_message(message.from_user.id, 'Ты в моей базе данных-_-')
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        users_db_add(user_id=us_id, user_name=us_name)


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
        bot.send_audio('788152184', src)


'''@bot.message_handler(content_types=['text']) == 'approve_this_audio_99'
def moderation_code(message, res=False):
    mod = 1
    music_db_mod(music_id=id())'''


bot.polling(none_stop=True)
