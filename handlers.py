from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command
from keyboards import keyboard, keyboard1, phone_key, mac_key
from main import bot, dp
from aiogram.dispatcher import FSMContext
from shop import Shop, price1, price2

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


# Section: ShopApp
@dp.message_handler(Command('buy'), state=None)
async def shop(message: Message):
    await message.answer('Какой товар вы хотите купить 1 или 2')
    await Shop.step1.set()


@dp.message_handler(state=Shop.step1)
async def shop(message: Message, state: FSMContext):
    item = message.text

    await state.update_data(
        {
            'item': item
        }
    )

    await message.answer('Сколько?')
    await Shop.next()


@dp.message_handler(state=Shop.step2)
async def count(message: Message, state: FSMContext):
    data = await state.get_data()
    item = data.get('item')
    if item == '1':
        p = price1
    else:
        p = price2

    count = int(message.text)

    await message.answer(f'Отлично! с вас {p * count}')
    await state.finish()
