from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text, Command
from keyboards import keyboard

from main import bot, dp

from config import chat_id


async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='Hello')


@dp.message_handler(Command('shop'))
async def show_shop(msg: Message):
    await msg.answer('Shop', reply_markup=keyboard)


@dp.message_handler(Text(equals=['btn1', 'btn2', 'btn3']))
async def get_goods(msg: Message):
    await msg.answer(msg.text, reply_markup=ReplyKeyboardRemove())
