from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command
from keyboards import keyboard, keyboard1, phone_key, mac_key
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


@dp.message_handler(Command('tshop'))
async def show(msg: Message):
    await msg.answer(text='Покупка или отмена', reply_markup=keyboard1)


@dp.callback_query_handler(text_contains='phone')
async def phone(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Купить', reply_markup=phone_key)


@dp.callback_query_handler(text_contains='mac')
async def macbook(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Купить', reply_markup=mac_key)


@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('Отмена', show_alert=True)

    await call.message.edit_reply_markup(reply_markup=None)
