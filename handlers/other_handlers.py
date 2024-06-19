from aiogram import Router
from aiogram.types import Message
from keyboards.keyboards import yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['other_answer'],
        reply_markup=yes_no_kb
        )
