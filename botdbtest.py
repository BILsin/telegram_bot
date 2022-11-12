import telebot, time, schedule


bot = telebot.TeleBot('5747352743:AAFNu1qNIA1i-Gaft71cwZqRTAz34JnxZGg')
k = 1


@bot.message_handler(content_types=['audio'])
def handle_docs_photo(message):
    try:
        file_info = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src ='C:/' + file_info.file_path
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.reply_to(message, "Аудио добавлено")
    except Exception as e:
        bot.reply_to(message, e)


def send_message():
    bot.send_message('788152184', 'время кушац')


schedule.every().day.at("21:59").do(send_message)


while True:
    schedule.run_pending()
    time.sleep(1)


bot.polling(none_stop=True)
