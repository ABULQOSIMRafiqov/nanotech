from aiogram.dispatcher.filters.state import StatesGroup, State


class Data(StatesGroup):
    raqam = State()
    ism = State()
    kurs = State()
    kursga_yozilish = State()
    tasdiqlash = State()
