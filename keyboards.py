from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from config import URL_MAC, URL_IPHONE

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='btn1'), KeyboardButton(text='btn2')],
        [KeyboardButton(text='btn3')]
    ],
    resize_keyboard=True
)

cb = CallbackData('buy', 'id', 'name', 'price')
keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Iphone', callback_data='buy:0:phone:2000'),
            InlineKeyboardButton(text='MacBook', callback_data='buy:0:mac:3000')
        ],
        [
            InlineKeyboardButton(text='cancel', callback_data='cancel')
        ]
    ]
)


phone_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Купить', url=URL_IPHONE)
        ]
    ]
)

mac_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Купить', url=URL_MAC)
        ]
    ]
)
