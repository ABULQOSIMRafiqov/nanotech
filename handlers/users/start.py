from ast import If
from cgitb import text
from lib2to3.pgen2.token import EQUAL
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Text
from loader import dp, bot
from keyboards.default.tugmalar import kurslar, raqam, yozilish
from keyboards.inline.inline_tugmalar import tasdiqlash
from states.holatlar import Data


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! <b>Niners Academyning rasmiy botiga</b> xush kelibsiz ☺️.\n Marhamat, ro'yxatdan o'tish uchun telefon raqamingizni jo'nating.", reply_markup=raqam)
    await Data.raqam.set()





@dp.message_handler(state=Data.raqam, content_types=types.ContentTypes.CONTACT)
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(
        {"phone": message.contact.phone_number}
    )
    await message.answer("<b>Raqam qabul qilindi 😉</b>\n\nIsm va familiyangizni kiriting.", reply_markup=types.ReplyKeyboardRemove())
    await Data.ism.set()


@dp.message_handler(state=Data.ism, content_types=types.ContentTypes.TEXT)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(
        {"full_name": message.text}
    )
    await message.answer("<b>Ism va familiya qabul qilindi.</b>\n\nKurslardan birini tanlang.", reply_markup=kurslar)
    await Data.kurs.set()
#



@dp.message_handler(text="Ortga", state="*")
async def cancel(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(text='Menuni tanlang', reply_markup=kurslar)

@dp.message_handler(state=Data.kurs)
async def about(msg: types.Message, state: FSMContext):
    if msg.text == "IELTS Complete(4,5 - 6.0 😌)":
        await state.update_data({
            "course_name": msg.text
        })
        await msg.answer(text="""IELTS Complete kursi:

✅Umumiy 32 ta darsdan iborat bo'lib, o'rtacha hisobda 2.5 oydan ko'proq davom etadi.

🔥Kursga yozilish uchun hozirgi darajasi eng kamida 4.5 bo'lishi yoki Niners Academy Pre-IELTS  kursini tugatgan bo'lishi zarur. IELTS haqida tushuncha bo'lmasa, lekin grammatika tugatilgan bo'lsa ham ushbu kursga to'g'ri keladi.

1️⃣Kursda 4 ta skill bo'yicha umumiy tushunchalar beriladi va amalda qanday qo'llash mumkinligi birma-bir ko'rsatiladi. 

2️⃣Kurs o'quvchilari har oy "Free Mock" da qatnashib olgan bilimlarini sinab ko'rishlari mumkin.

💯Kursning asosiy maqsadi: IELTS intensive kurslari uchun kuchli bazage ega o'quvchini tayyorlash.

📌Kursni tugatib imtihon topshirish: Tavsiya etilmaydi chunki o'zi maqsad qilgan natijaga erisha olmasligi mumkin. Odatda complete ni tugatga o'quvchilar 5.5-6.0 atrofida yoki CEFR imtihonidan B2 darajani oladilar.

🔜Kurs to'lovi: oylik 420.000

Darslar qachondan boshlanishi haqida batafsil malumotni 979147914 raqamiga aloqaga chiqib batafsil malumot olishingiz mumkin.""", reply_markup=yozilish)
        await Data.kursga_yozilish.set()
    elif msg.text == "IELTS Intensive(5,5-7+ 😎)":
        await msg.answer(text="""IELTS intensive kursi.

✅Umumiy 24 ta darsdan iborat bo'lib, o'rtacha hisobda 2 oy davom etadi.

❗️Kursga yozilish uchun hozirgi darajasi eng kamida 5.5 bo'lgan yoki Niners Academyda "IELTS Masterclass" darajasini tugatgan bo'lishi shart.

1️⃣Kursda 4 ta skilldan barcha savol turlari to'liq ko'rib chiqilib amaliy tarzda darslarda tahlil qilish asosida mustahkamlanadi.

2️⃣Kursda dars o'tadigan asosiy instructor o'quvchilarga bo'sh vaqtini samarali o'tkazish uchun "Self Study" e-resurslari bilan taminlaydi.

3️⃣Kurs o'quvchilari har oy "Free Mock" da qatnashib darajalarini aniqlab olishlari mumkin.

💯Kursning asosiy maqsadi 1 oyga +1 ballga ko'tarish hisoblanadi.

📌Agarda barcha vazifalar bajarilsa, ushbu natija olinishiga kafolat beriladi. Dars sifati va olib borilishi bo'yicha muammo bo'lishi mumkin emas

🔜Kurs to'lovi: oylik 420.000 so'm

  Darslar qachondan boshlanishi haqida batafsil malumotni 979147914 raqamiga aloqaga chiqib batafsil malumot olishingiz mumkin.""", reply_markup=yozilish)
        await state.update_data({
            "course_name": msg.text
        })
        await Data.kursga_yozilish.set()
    else:
        await msg.answer("Mavjud kurslardan birini tanlang: ", reply_markup=kurslar)
    
    

@dp.message_handler(text='Kursga yozilish', state=Data.kursga_yozilish)
async def course(message: types.Message, state:FSMContext):


    data = await state.get_data()
    ismFamilya = data.get("full_name")
    telefonRaqam = data.get("phone")
    kursNomi = data.get("course_name")
    msg = "<b>Quyidagi ma'lumotlar qabul qilindi:</b>\n"
    msg += f"<b>To'liq ism:</b> {ismFamilya}\n"
    msg += f"<b>Telefon raqam:</b> {telefonRaqam}\n"
    msg += f"<b>Tanlangan kurs:</b> {kursNomi}\n\n"
    msg += f"<b>Shu ma'lumotlar tog'rimi?🤔</b>"
    await message.answer(text=msg, reply_markup=tasdiqlash)
    await Data.tasdiqlash.set()
    


    
@dp.callback_query_handler(state=Data.tasdiqlash)
async def tasdiqlovchi(message: types.CallbackQuery, state: FSMContext):
    await message.answer(cache_time=1)
    query = message.data
    if query == "yes":
        data = await state.get_data()
        ismFamilya = data.get("full_name")
        telefonRaqam = data.get("phone")
        kursNomi = data.get("course_name")
        userId = data.get("id")
        msg = "Ma'lumotlar qabul qilindi, siz bilan menejerlarimiz qisqa fursatda bog'lanishadi 😊"
        await bot.send_message(chat_id=message.from_user.id, text=msg)
        await bot.send_message(chat_id=1154548972, text=f"<b>Quyidagi foydalanuvchi kursga ro'yxatdan o'tish uchun murojaat qildi:</b>\n\nIsm:<a href='tg://user?id={userId}'>{ismFamilya}</a>\nRaqam: {telefonRaqam}\nKurs: {kursNomi}")
        await state.finish()

    else:
        await state.finish()
        await message.answer("Ma'lumotlar o'chirildi.")
        await bot.send_message(chat_id=message.from_user.id, text="Qayta ro'yxatdan o'tish uchun /register buyrug'ini kiriting.")
