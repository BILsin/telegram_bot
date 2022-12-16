import telebot
from telebot import types
import random
import shutil
import os
import glob


b = open('music_number.txt')
music_number = int(b.readline())


def random_number():
    k = 0
    c = []
    while k != 5:
        if k == 5:
            break
        fileop = open('music_number.txt')
        X = random.randrange(0, int(fileop.readline()))
        if c.count(X) == 0:
            c.append(X)
        elif len(c) == 5:
            break
        else:
            continue
    return c


c = random_number()
print(c)


papka2 = glob.glob(r'C:\Users\фвьшт\OneDrive\Работа\Python\GitHub\telegram_bot\winner\*')
for j in papka2:
    os.remove(j)
print('winner очищен')


sch = open('like1.txt')
likeinf1 = int(sch.readline())
sch = open('like2.txt')
likeinf2 = int(sch.readline())
sch = open('like3.txt')
likeinf3 = int(sch.readline())
sch = open('like4.txt')
likeinf4 = int(sch.readline())
sch = open('like5.txt')
likeinf5 = int(sch.readline())


n = open('c.txt')
st = n.readline()
cold = st.split()
print(cold)
winner = max(likeinf1, likeinf2, likeinf3, likeinf4, likeinf5)
if winner == likeinf1:
    maximum = 0
if winner == likeinf2:
    maximum = 1
if winner == likeinf3:
    maximum = 2
if winner == likeinf4:
    maximum = 3
if winner == likeinf5:
    maximum = 4
print(winner, maximum)
shutil.copy(os.path.join('C:\music', 'music' + str(cold[maximum]) + '.mp3'), r'C:\Users\фвьшт\OneDrive\Работа\Python\GitHub\telegram_bot\winner')
os.rename(r'C:\Users\фвьшт\OneDrive\Работа\Python\GitHub\telegram_bot\winner\music' + str(cold[maximum]) + '.mp3', r'C:\Users\фвьшт\OneDrive\Работа\Python\GitHub\telegram_bot\winner\winner.mp3')
print('победитель определён')


with open('like1.txt', 'w') as n:
    n.write(str(0))
with open('like2.txt', 'w') as n:
    n.write(str(0))
with open('like3.txt', 'w') as n:
    n.write(str(0))
with open('like4.txt', 'w') as n:
    n.write(str(0))
with open('like5.txt', 'w') as n:
    n.write(str(0))


papka = glob.glob(r'C:\Users\фвьшт\OneDrive\Работа\Python\GitHub\telegram_bot\leadervote\*')
for f in papka:
    os.remove(f)
print('leadervote очищен')


for i in range(0, 5):
    shutil.copy(os.path.join('C:\music', 'music' + str(c[i]) + '.mp3'), r'C:\Users\фвьшт\OneDrive\Работа\Python\GitHub\telegram_bot\leadervote')
print('файлы скопированы')


with open(r"C:\Users\фвьшт\OneDrive\Работа\Python\GitHub\telegram_bot\c.txt", "w") as n:
    n.write(str(c[0])+' '+str(c[1])+' '+str(c[2])+' '+str(c[3])+' '+str(c[4]))


likeprofile = []
bot = telebot.TeleBot('5883195717:AAGsI3Jp8Vu79h0ubIg7sZmRUExvalAo9DY')


@bot.message_handler(commands=['start'])
def start_message(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1000 = types.KeyboardButton("Обратная связь")
    btn999 = types.KeyboardButton("Посмотреть список на сегодня")
    btn993 = types.KeyboardButton("Как предложить свою мелодию?")
    murkup.add(btn999, btn1000, btn993)
    bot.send_message(message.chat.id, text="Здравствуйте,{0.first_name}!\nВас приветствует телеграмм бот, который может менять школьные звонки посредством голосования. Что бы аудио прошло модерацию нужно соблюдать несколько правил: \n1.Audio файл должен быть от 8-15 секунд   \n2.Файл не должен содержать мата, резких и режущих звуков. \nДля загрузки просто отправьте аудио боту".format(message.from_user), reply_markup=murkup)


@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    global music_number, n
    file_info = bot.get_file(message.audio.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    bot.send_audio('788152184', downloaded_file)
    bot.reply_to(message, 'Аудио добавлено')
    if message.from_user.id == 788152184 or message.from_user.id == 5883195717:
        with open(r"C:\music\music" + str(music_number) + ".mp3", 'wb') as new_file:
            with open('music_number.txt', 'w') as n:
                music_number += 1
                n.write(str(music_number))
            new_file.write(downloaded_file)


@bot.message_handler(content_types=['text'])
def priziv(message):
    global c
    if message.chat.type == 'private':
        if message.text == 'Как предложить свою мелодию?':
            bot.send_message(message.chat.id, "Что бы предложить свою мелодию просто отправь боту аудио файл. Он отправиться на модерацию, и если он подходит по всем критериям, то будет добавлен!\nКритерии к аудио:\n1. Длительность от 8 до 15 секунд.\n2. Без мата, неожиданных, неприятных и прочих нецензурных слов/звуков\nЕсли ваше аудио дольше 15 секунд, вы можете обрезать его на этом сайте: https://mp3cut.net/ru/\nНайти музыку вам может помочь этот бот: https://t.me/music_telebot")
        if message.text == "Посмотреть список на сегодня":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(1, callback_data="bt1")
            markup.add(button1)
            with open('C:\\music\\music' + str(c[0]) + '.mp3', 'rb') as f:
                bot.send_audio(message.chat.id, f)
            bot.send_message(message.chat.id, 'Лайк'.format(message.from_user), reply_markup=markup)
            markup = types.InlineKeyboardMarkup()
            button2 = types.InlineKeyboardButton(2, callback_data="bt2")
            markup.add(button2)
            with open('C:\\music\\music' + str(c[1]) + '.mp3', 'rb') as f:
                bot.send_audio(message.chat.id, f)
            bot.send_message(message.chat.id, 'Лайк'.format(message.from_user), reply_markup=markup)
            markup = types.InlineKeyboardMarkup()
            button3 = types.InlineKeyboardButton(3, callback_data="bt3")
            markup.add(button3)
            with open('C:\\music\\music' + str(c[2]) + '.mp3', 'rb') as f:
                bot.send_audio(message.chat.id, f)
            bot.send_message(message.chat.id, 'Лайк'.format(message.from_user), reply_markup=markup)
            markup = types.InlineKeyboardMarkup()
            button4 = types.InlineKeyboardButton(4, callback_data="bt4")
            markup.add(button4)
            with open('C:\\music\\music' + str(c[3]) + '.mp3', 'rb') as f:
                bot.send_audio(message.chat.id, f)
            bot.send_message(message.chat.id, 'Лайк'.format(message.from_user), reply_markup=markup)
            markup = types.InlineKeyboardMarkup()
            button5 = types.InlineKeyboardButton(5, callback_data="bt5")
            markup.add(button5)
            with open('C:\\music\\music' + str(c[4]) + '.mp3', 'rb') as f:
                bot.send_audio(message.chat.id, f)
            bot.send_message(message.chat.id, 'Лайк'.format(message.from_user), reply_markup=markup)
        if message.text == 'Обратная связь':
            bot.send_message(message.chat.id, 'https://docs.google.com/forms/d/e/1FAIpQLSfnp-w2O2mvRjvA1Y0QBUKO-b1M_tVbtR-CFhk3B2dLcV4YoQ/viewform?usp=sf_link'.format(message.from_user))


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    print(likeprofile)
    if call.data == 'bt1':
        if likeprofile.count(call.from_user.id) == 0:
            likeprofile.append(call.from_user.id)
            n = open('like1.txt')
            like = n.readline()
            like = str(int(like) + 1)
            with open('like1.txt', 'w') as n:
                n.write(str(like))
            bot.send_message(call.message.chat.id, 'Лайк засчитан. Колличество лайков у выбранного трека:' + ' ' + str(like))
        else:
            bot.send_message(call.message.chat.id, 'Ты уже лайкал сегодня')
    if call.data == 'bt2':
        if likeprofile.count(call.from_user.id) == 0:
            likeprofile.append(call.from_user.id)
            n = open('like2.txt')
            like = n.readline()
            like = str(int(like) + 1)
            with open('like2.txt', 'w') as n:
                n.write(str(like))
            bot.send_message(call.message.chat.id, 'Лайк засчитан. Колличество лайков у выбранного трека:' + ' ' + str(like))
        else:
            bot.send_message(call.message.chat.id, 'Ты уже лайкал сегодня')
    if call.data == 'bt3':
        if likeprofile.count(call.from_user.id) == 0:
            likeprofile.append(call.from_user.id)
            n = open('like3.txt')
            like = n.readline()
            like = str(int(like) + 1)
            with open('like3.txt', 'w') as n:
                n.write(str(like))
            bot.send_message(call.message.chat.id, 'Лайк засчитан. Колличество лайков у выбранного трека:' + ' ' + str(like))
        else:
            bot.send_message(call.message.chat.id, 'Ты уже лайкал сегодня')
    if call.data == 'bt4':
        if likeprofile.count(call.from_user.id) == 0:
            likeprofile.append(call.from_user.id)
            n = open('like4.txt')
            like = n.readline()
            like = str(int(like) + 1)
            with open('like4.txt', 'w') as n:
                n.write(str(like))
            bot.send_message(call.message.chat.id, 'Лайк засчитан. Колличество лайков у выбранного трека:' + ' ' + str(like))
        else:
            bot.send_message(call.message.chat.id, 'Ты уже лайкал сегодня')
    if call.data == 'bt5':
        if likeprofile.count(call.from_user.id) == 0:
            likeprofile.append(call.from_user.id)
            n = open('like5.txt')
            like = n.readline()
            like = str(int(like) + 1)
            with open('like5.txt', 'w') as n:
                n.write(str(like))
            bot.send_message(call.message.chat.id, 'Лайк засчитан. Колличество лайков у выбранного трека:' + ' ' +str(like))
        else:
            bot.send_message(call.message.chat.id, 'Ты уже лайкал сегодня')


bot.polling(none_stop=True)
