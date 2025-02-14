import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import TelegramAPIError

# تنظیمات لاگ‌گیری برای خطایابی
logging.basicConfig(level=logging.INFO)

# توکن ربات تلگرام
API_TOKEN = "7746983847:AAHj7bO_3io6OyiZ-PsYMl0QxGStg-_3R6k"

# شناسه کانال (با @ بنویس)
CHANNEL_ID = "@crushyab_bam"

# مقداردهی ربات و دیسپچر
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# تابع بررسی عضویت کاربر در کانال
async def check_membership(user_id):
    try:
        member = await bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except TelegramAPIError:
        return False

# هندلر /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_user.id

    # پیام خوش‌آمدگویی
  welcome_text = "\U0001F44B به ربات کراش‌یاب بم خوش آمدید!\n\n\U0001F539 این ربات به شما کمک می‌کند تا کراش خود را پیدا کنید. اما قبل از شروع، ابتدا باید عضو کانال ما شوید. \U00002705"
member_text = "\U00002705 شما عضو کانال هستید، حالا می‌توانید از ربات استفاده کنید!"
    await message.answer(welcome_text)

    # بررسی عضویت کاربر
    is_member = await check_membership(user_id)
    
    if is_member:
        await message.answer(":white_check_mark: شما عضو کانال هستید، حالا می‌توانید از ربات استفاده کنید!")
    else:
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton(":loudspeaker: عضویت در کانال", url=f"https://t.me/{CHANNEL_ID[1:]}"))
        keyboard.add(InlineKeyboardButton(":white_check_mark: عضو شدم", callback_data="check_membership"))

        await message.answer(":warning: برای استفاده از ربات، ابتدا باید عضو کانال ما شوید.", reply_markup=keyboard)

# بررسی دکمه "عضو شدم"
@dp.callback_query_handler(lambda c: c.data == "check_membership")
async def verify_membership(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_member = await check_membership(user_id)
    
    if is_member:
        await bot.answer_callback_query(callback_query.id, ":white_check_mark: عضویت تأیید شد!")
        await bot.send_message(user_id, ":white_check_mark: حالا می‌توانید از ربات استفاده کنید!")
    else:
        await bot.answer_callback_query(callback_query.id, ":x: هنوز عضو کانال نشده‌اید!")

# اجرای ربات
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

