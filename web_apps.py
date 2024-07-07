from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
bot = Bot('7022880490:AAETS1y4rA8pXU-a4-spXNIOQM5KlGbTRN8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://people.com/music/j-hope-of-bts-says-performing-as-a-solo-artist-is-challenging-but-fun/')))
    await message.answer('Привет, мой друг!', reply_markup=markup)

executor.start_polling(dp)
