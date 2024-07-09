from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('BOT_TOKEN', '').strip()
payment_token = os.getenv('PAYMENT_TOKEN', '').strip()

if not bot_token or not payment_token:
    raise ValueError("BOT_TOKEN или PAYMENT_TOKEN не найдены в окружении")

bot = Bot(bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_invoice(
        message.chat.id,
        title='Покупка курса',
        description='Покупка курса Python',
        payload='invoice',
        provider_token=payment_token,
        currency='USD',
        prices=[types.LabeledPrice(label='Покупка курса', amount=5 * 100)]
    )


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def success(message: types.Message):
    await message.answer(f'Success: {message.successful_payment.order_info}')

executor.start_polling(dp)
