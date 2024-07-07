import telebot
import requests
import json

bot = telebot.TeleBot('7022880490:AAETS1y4rA8pXU-a4-spXNIOQM5KlGbTRN8')
API = '5e1414115ead86363c93f75fab5537da'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рада тебя видеть! Напишите название города: ')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')

        image = 'нагиса.jpg' if temp > 20.0 else 'ff.jpg'
        file = open('./data/' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан не верно')


bot.polling(none_stop=True)
