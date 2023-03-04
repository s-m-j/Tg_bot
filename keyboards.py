from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='btn1'), KeyboardButton(text='btn2')],
        [KeyboardButton(text='btn3')]
    ],
    resize_keyboard=True
)