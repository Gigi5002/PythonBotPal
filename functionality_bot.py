import telebot
from telebot import types
import webbrowser
bot = telebot.TeleBot('7022880490:AAETS1y4rA8pXU-a4-spXNIOQM5KlGbTRN8')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    file = open('data/men_kyrgyz.jpg', 'rb')
    # bot.send_photo(message.chat.id, file, reply_markup=markup)  # ./men_kyrgyz.jpg
    # bot.send_audio(message.chat.id, file, reply_markup=markup)  # ./men_kyrgyz.mp3
    # bot.send_video(message.chat.id, file, reply_markup=markup)  # ./men_kyrgyz.mp4
    # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Deleted')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://trello.com/b/2Hz9jyDw/work')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Просто фантастика!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://pypi.org/project/pyTelegramBotAPI/')


@bot.message_handler(commands=['start', 'salam', 'hello', 'привет'])
def main(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help me please!!!!!</b> <em><u>-zdohni</u></em>', parse_mode='HTML')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'Салам!':
        bot.send_message(message.chat.id, f'Салам {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)