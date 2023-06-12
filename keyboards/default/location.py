from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


location_keyborad = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Joylashuv 📍", request_location=True)
        ]
    ],
    resize_keyboard=True
)