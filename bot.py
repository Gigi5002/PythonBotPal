import telebot
from telebot import types

bot = telebot.TeleBot('7022880490:AAETS1y4rA8pXU-a4-spXNIOQM5KlGbTRN8')

name = ''
surname = ''
age = 0

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Не запомню :(')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    summary = f'Тебе {age} лет, тебя зовут {name} {surname}. Всё правильно?'
    markup = types.InlineKeyboardMarkup()
    yes_button = types.InlineKeyboardButton(text='Да', callback_data='yes')
    no_button = types.InlineKeyboardButton(text='Нет', callback_data='no')
    markup.add(yes_button, no_button)
    bot.send_message(message.from_user.id, summary, reply_markup=markup)

bot.polling(none_stop=True, interval=0)

# @bot.message_handler(content_types=['text', 'document', 'audio'])
# def get_text_message(message):
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши Привет!")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")
