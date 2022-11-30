import telebot


bot = telebot.TeleBot('5909965445:AAFEL1bZUOxr65V8Re200stoauIQg8yvLSE')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, '1.Предлагаю всем встать')
    bot.send_message(message.from_user.id, '2.Учимся сгибать колени. Присядьте')
    bot.send_message(message.from_user.id, '3.Теперь надо опять встать')
    bot.send_message(message.from_user.id, '4.Теперь найдите предоставленный нами стул. Он должен быть прямо за вами')
    bot.send_message(message.from_user.id, '5.Следующий шаг - подойдите вплотную к стулу, так чтобы его сиденье упиралось вам в задние части колен')
    bot.send_message(message.from_user.id, '6.Согните колени')
    bot.send_message(message.from_user.id, 'Поздравляем! Вы добились поставленной цели')
    bot.send_message(message.from_user.id, '7.Теперь встаньте, отложите телефон и попробуйте применить полученые навыки без инструкции на другом стуле')
    bot.send_message(message.from_user.id, '8.В случае неудачи- перечитайте инструкцию')


bot.polling(none_stop=True)
