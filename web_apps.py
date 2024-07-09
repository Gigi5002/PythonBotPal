from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json
bot = Bot('7022880490:AAETS1y4rA8pXU-a4-spXNIOQM5KlGbTRN8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://www.google.com/search?client=ubuntu-sn&hs=WQp&sca_esv=6ebf0840f301bbeb&channel=fs&sxsrf=ADLYWILQfN9l5MCrtTZEZD1krkIN9jOnQg:1720431816944&q=%D0%90%D0%B7%D1%83%D0%BB%D0%B0&udm=2&fbs=AEQNm0DDgaHKHmgQPgdfMPlZgxGLwuE-BIysBnISHvAJaP-1wJKQFapmC2DUhIT38gZnZpw1zSnVyaQ81y53VpJmuSGqbd0rjTW8ni68i5j9Efk4daGQ1GdZAuvRQUraap-nNfPv0J9so9iUrNFl4EoJ9ZgdV3REl-PeKmdhltWknQTqqiKTMQWyFuS4--LumN00NbGrg-Kavu-HA-f4LUNjocR7UYsEegflBfvapgq1EDW-jjN429M&sa=X&ved=2ahUKEwjCtLz6k5eHAxX-CBAIHel_BJsQtKgLegQIDhAB&biw=911&bih=902&dpr=1#vhid=TvgnhHRlb9pzwM&vssid=mosaic')))
    await message.answer('Привет, мой друг!', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}')

executor.start_polling(dp)
