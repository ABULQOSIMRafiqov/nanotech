from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tasdiqlash = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha", callback_data='yes'),
            InlineKeyboardButton(text="Yo'q", callback_data='no')
        ]
    ]
)
