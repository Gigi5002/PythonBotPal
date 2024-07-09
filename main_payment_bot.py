from aiogram import Bot, Dispatcher, executor, types
import payment_bot

bot = Bot(payment_bot.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_invoice(message.chat.id, 'Покупка курса', 'Покупка курса Python', 'invoice', payment_bot.PAYMENT_TOKEN, 'USD', [types.LabeledPrice('Покупка курса', 5 * 100)])


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def success(message: types.Message):
    await message.answer(f'Success: {message.successful_payment.order_info}')


executor.start_polling(dp)
