import asyncio
import os
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# .env файлынан айнымалыларды жүктеу
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Логтарды баптау (қателерді бақылау үшін)
logging.basicConfig(level=logging.INFO)

# Боты мен Диспетчерді инициализациялау
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- КЛАВИАТУРА ---
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Біз туралы")],
        [KeyboardButton(text="Бағыттар"), KeyboardButton(text="Байланыстар")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Мәзірден бөлімді таңдаңыз..."
)

# --- ХЭНДЛЕРЛЕР (ӨҢДЕУШІЛЕР) ---

# /start командасы
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    welcome_text = (
        f"Сәлеметсіз бе, {message.from_user.first_name}!\n\n"
        "**Жастар ресурстық орталығының** ресми ботына кош келдіңіз!\n"
        "Төмендегі батырмалар арқылы қажетті ақпаратты ала аласыз:"
    )
    await message.answer(welcome_text, reply_markup=main_keyboard, parse_mode="Markdown")

# "Біз туралы" батырмасы
@dp.message(F.text == "Біз туралы")
async def about_us(message: types.Message):
    text = (
        "**🏛 Жастар ресурстық орталығы туралы**\n\n"
        "Жастар ресурстық орталығы — жастардың бастамаларын қолдауға, "
        "тұлғалық және кәсіби дамуына, сондай-ақ әлеуметтік бейімделуіне көмектесетін мемлекеттік мекеме.\n\n"
        "**Біздің мақсатымыз:** Жастардың әлеуетін ашуға қолайлы орта өңдеу және "
        "мемлекеттік жастар саясатын тиімді жүзеге асыру."
    )
    await message.answer(text, parse_mode="Markdown")

# "Бағыттар" батырмасы
@dp.message(F.text == "Бағыттар")
async def directions(message: types.Message):
    text = (
        "**📌 Негізгі жұмыс бағыттарымыз:**\n\n"
        "1. **Жастар бастамаларын қолдау:** Гранттар, жобалар мен стартаптарға көмек.\n"
        "2. **Волонтерлік қозғалыс:** Қайырымдылық және әлеуметтік акциялар.\n"
        "3. **Кәсіби бағдар беру және жұмыспен қамту:** Бос орындар жарменкесі, курстар.\n"
        "4. **Құқықтық және психологиялық кеңес:** Жастарға тегін көмек көрсету.\n"
        "5. **Мәдени-бұқаралық және спорттық шаралар:** Дебаттар, турнирлер, тренингтер."
    )
    await message.answer(text, parse_mode="Markdown")

# "Байланыстар" батырмасы
@dp.message(F.text == "Байланыстар")
async def contacts(message: types.Message):
    text = (
        "**📞 Байланыс ақпараты:**\n\n"
        "📍 **Мекенжайымыз:** [Қала, көше атауы, үй нөмірі]\n"
        "📞 **Телефон:** +7 (7xx) xxx-xx-xx\n"
        "✉️ **Email:** info@mrc.kz\n"
        "🌐 **Сайт:** https://mrc.kz\n"
        "📱 **Instagram:** @mrc_official\n\n"
        "⏰ **Жұмыс уақыты:** Дүйсенбі - Жұма, 09:00 - 18:30 (Үзіліс: 13:00 - 14:30)"
    )
    await message.answer(text, parse_mode="Markdown")

# --- БОТТЫ ІСКЕ ҚОСУ ---
async def main():
    # Бот өшіп тұрғанда келген ескі хабарламаларды тазалау
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())