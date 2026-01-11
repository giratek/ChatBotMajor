import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN environment variable not set!")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def start(msg: types.Message):
    await msg.answer("Привет! Я бот, и я живу на Railway 🚂")

@dp.message_handler()
async def echo(msg: types.Message):
    await msg.answer("Ты написал: " + msg.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
