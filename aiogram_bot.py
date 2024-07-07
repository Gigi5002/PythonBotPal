from aiogram import Bot, Dispatcher, executor, types

bot = Bot('7022880490:AAETS1y4rA8pXU-a4-spXNIOQM5KlGbTRN8')
dp = Dispatcher(bot)


@dp.message_handler(content_types=['photo'])  # commands=['start']
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Hello') обычно выводит сообщения)
    # await message.answer('Hello') обычно выводит сообщения)
    await message.reply('Hello')  # отвечает на сообщение
    # file = open('/some.jpg', 'rb') открывает файл
    # await message.answer_photo(file) отправляет файл


@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()  # row_wiath-количество кнопок в одном ряду
    markup.add(types.InlineKeyboardButton('Site', url='https://trello.com/b/2Hz9jyDw/work'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)


@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)


@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.answer('Hello', reply_markup=markup)


executor.start_polling(dp)
