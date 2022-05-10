from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kurslar = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='IELTS Complete(4,5 - 6.0 😌)'),
            KeyboardButton(text='IELTS Intensive(5,5-7+ 😎)')
        ],
    #    [
     #       KeyboardButton(text='B1'),
     #       KeyboardButton(text='B2')
       # ],
       # [
        #    KeyboardButton(text='C1')
       # ]
    ]
)

raqam = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Raqamni jo'natish", request_contact=True)
        ]
    ]
)

yozilish = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Kursga yozilish")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ]
)

yozilish = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Kursga yozilish")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ]
)
