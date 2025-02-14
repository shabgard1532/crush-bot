from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio

# توکن ربات را اینجا بگذارید
API_TOKEN = "7746983847:AAHj7bO_3io6OyiZ-PsYMl0QxGStg-_3R6k"

# ایجاد نمونه‌های ربات و دیسپچر
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# هندلر برای دستور /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("سلام! ربات کراش‌یاب آماده است. :blush:")

# اجرای ربات
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
