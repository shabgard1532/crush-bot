import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import TelegramAPIError

# تنظیمات لاگ‌گیری برای خطایابی
logging.basicConfig(level=logging.INFO)

# :small_blue_diamond: توکن ربات (حتماً مقدارش را تنظیم کن)
API_TOKEN = "7746983847:AAHj7bO_3io6OyiZ-PsYMl0QxGStg-_3R6k"

# :small_blue_diamond: شناسه کانال (بدون @ ننویس)
CHANNEL_ID = "@crushyab_bam"

# مقداردهی ربات و دیسپچر
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# :small_blue_diamond: تابع بررسی عضویت کاربر در کانال
async def check_membership(user_id):
    try:
        member = await bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except TelegramAPIError:
        return False

# :small_blue_diamond: هندلر /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_user.id

    # :tada: پیام خوش‌آمدگویی
    welcome_text = (
        ":👋 به ربات کراش‌یاب بم خوش آمدید!\n\n"
        ": 💘 در این ربات می‌توانید کراش خود را پیدا کنید.\n"
        ":🔹: اما قبل از شروع، لطفاً عضو کانال ما شوید. ✅:"
    )
    await message.answer(welcome_text)

    # :small_blue_diamond: بررسی عضویت کاربر
    is_member = await check_membership(user_id)
    
    if is_member:
        await message.answer(":white_check_mark: شما عضو کانال هستید، حالا می‌توانید از ربات استفاده کنید! :speech_balloon:")
    else:
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton(":loudspeaker: عضویت در کانال", url=f"https://t.me/{CHANNEL_ID[1:]}"))
        keyboard.add(InlineKeyboardButton(":white_check_mark: عضو شدم", callback_data="check_membership"))

        await message.answer(":warning: برای استفاده از ربات، ابتدا باید عضو کانال ما شوید. :point_down:", reply_markup=keyboard)

# :small_blue_diamond: بررسی دکمه ":white_check_mark: عضو شدم"
@dp.callback_query_handler(lambda c: c.data == "check_membership")
async def verify_membership(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_member = await check_membership(user_id)
    
    if is_member:
        await bot.answer_callback_query(callback_query.id, ":white_check_mark: عضویت شما تأیید شد! :tada:")
        await bot.send_message(user_id, ":white_check_mark: حالا می‌توانید از ربات استفاده کنید! :speech_balloon:")
    else:
        await bot.answer_callback_query(callback_query.id, ":x: هنوز عضو کانال نشده‌اید! :name_badge:")

# :small_blue_diamond: اجرای ربات
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


