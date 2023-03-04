from aiogram.types import Message

from main import bot, dp

from config import chat_id


async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='Hello')


@dp.message_handler()
async def send_answer(msg: Message):
    text = msg.text
    # Можно было sendMessage но туда надо передавать chat_id а answer отвечает в тот же чат
    await msg.answer(text=text)
