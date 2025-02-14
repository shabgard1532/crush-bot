import logging
from flask import Flask, request
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook

# توکن ربات رو اینجا بذار
API_TOKEN = "7746983847:AAHj7bO_3io6OyiZ-PsYMl0QxGStg-_3R6k"
WEBHOOK_URL = "https://crush-bot.onrender.com/webhook"
# تنظیمات وبهوک
WEBHOOK_HOST = "https://crush-bot.onrender.com"  # اینجا آدرس دامنه یا هاستت رو بذار
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# تنظیمات وب‌سرور
WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = 10000

# راه‌اندازی ربات
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# تنظیم لاگ‌ها
logging.basicConfig(level=logging.INFO)

# ساخت سرور Flask
app = Flask(__name__)

@app.route(WEBHOOK_PATH, methods=["POST"])
async def webhook_handler():
    update = types.Update(**request.json)
    await dp.process_update(update)
    return "OK", 200

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply :tada:("سلام! ربات وبهوک فعال شد")

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    await bot.delete_webhook()

if __name__ == "__main__":
    from aiogram import executor
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

