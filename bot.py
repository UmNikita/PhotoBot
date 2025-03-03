import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
import json

TOKEN = "7217191388:AAF-_q6UZeMK_SfyZFzAeffI-V3-PeEnCG0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

router = dp

with open("commands.json", "r", encoding="utf-8") as file:
    responses = json.load(file)

@router.message(Command("start"))
async def start_command(message: Message):
    mess = responses.get("startCommand", "").format(name=message.from_user.first_name)
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Забрать подарок🎁", callback_data="button_click")]
        ]
    )
    await message.answer(mess, reply_markup=keyboard)

@dp.callback_query(lambda c: c.data == "button_click")
async def button_response(callback: CallbackQuery):
    mess = responses.get("getLink", "")
    pay = responses.get("pay", "")
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Уже оплатил!")]
        ]
    )
    await callback.message.answer(mess)
    await callback.answer()

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())