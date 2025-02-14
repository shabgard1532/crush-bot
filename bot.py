om aiogram import Bot, Dispatcher, types from aiogram.utils import executor

توکن ربات رو اینجا بزار

API_TOKEN = "7746983847:AAHj7bO_3io6OyiZ-PsYMl0QxGStg-_3R6k"

bot = Bot(token=API_TOKEN) dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) async def start_command(message: types.Message): await message.reply("سلام! ربات کراش‌یاب آماده است")

if __name__ == '__main__': executor.start_polling(dp, skip_updates=True)
