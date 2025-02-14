from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from flask import Flask
import os

# توکن ربات رو اینجا بزار
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

    executor.start_polling(dp, skip_updates=True)
