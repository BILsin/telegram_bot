import telebot

token = '5747352743:AAFNu1qNIA1i-Gaft71cwZqRTAz34JnxZGg'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['audio'])
def handle_docs_photo(message):

    try:
        file_info = bot.get_file(message.audio[len(message.audio)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = '/mnt/files/tmp/'+file_info.file_path;
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.reply_to(message, "Аудио")

    except Exception as e:
        bot.reply_to(message, e)


bot.polling(none_stop=True)
