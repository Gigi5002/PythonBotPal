from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json
bot = Bot('7022880490:AAETS1y4rA8pXU-a4-spXNIOQM5KlGbTRN8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='http://localhost:63342/PythonPal/index.html?_ijt=qh22v4psv1gm347k68gasbqfie&_ij_reload=RELOAD_ON_SAVE')))
    # markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://76ea-212-112-111-37.ngrok-free.app')))
    await message.answer('Привет, мой друг!', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}')

executor.start_polling(dp)
