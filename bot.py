from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling
from flask import Flask
import asyncio
import os

# توکن ربات
API_TOKEN = "7746983847:AAHj7bO_3io6OyiZ-PsYMl0QxGStg-_3R6k"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("سلام! ربات کراش‌یاب آماده است. :blush:")

# سرور Flask برای Render
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

async def main():
    """ اجرای همزمان Flask و aiogram """
    loop = asyncio.get_event_loop()
    loop.create_task(start_polling(dp, skip_updates=True))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    asyncio.run(main())  # اجرای ربات
    app.run(host="0.0.0.0", port=port)  # اجرای Flask
