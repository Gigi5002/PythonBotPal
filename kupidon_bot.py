import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sqlite3

API_TOKEN = '7022880490:AAETS1y4rA8pXU-a4-spXNIOQM5KlGbTRN8'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

# Настройка базы данных
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, gender TEXT)''')
conn.commit()

# Состояния для анкеты
class Form(StatesGroup):
    name = State()
    age = State()
    gender = State()

# Обработчик команды /start
@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await Form.name.set()
    await message.reply("Как вас зовут?")

# Обработчик имени
@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Form.next()
    await message.reply("Сколько вам лет?")

# Обработчик возраста (проверка, что это число)
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def process_age_invalid(message: types.Message):
    return await message.reply("Возраст должен быть числом.\nСколько вам лет?")

@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = int(message.text)
    await Form.next()
    await message.reply("Какой у вас пол? (м/ж)")

# Обработчик пола
@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        cursor.execute("INSERT INTO users (name, age, gender) VALUES (?, ?, ?)",
                       (data['name'], data['age'], data['gender']))
        conn.commit()
    await state.finish()
    await message.reply("Анкета заполнена! Спасибо!")

# Обработчик команды /show_profiles для отображения анкет пользователей
@dp.message_handler(commands='show_profiles')
async def show_profiles(message: types.Message):
    cursor.execute("SELECT name, age, gender FROM users")
    users = cursor.fetchall()
    profiles = "\n".join([f"Имя: {user[0]}, Возраст: {user[1]}, Пол: {user[2]}" for user in users])
    await message.reply(f"Анкеты пользователей:\n{profiles}")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
