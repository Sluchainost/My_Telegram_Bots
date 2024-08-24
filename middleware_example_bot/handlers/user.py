import logging

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)
from filters.filters import MyFalseFilter, MyTrueFilter
from lexicon.lexicon import LEXICON_RU


# Инициализируем логгер модуля
logger = logging.getLogger()

# Инициализируем роутер уровня модуля
user_router = Router()


# Этот хендлер срабатывает на команду /start
@user_router.message(CommandStart(), MyTrueFilter())
async def process_start_command(message: Message):
    logger.debug('Вошли в хэндлер, обрабатывающий команду /start')
    # Создаем обьект инлайн-кнопки
    button = InlineKeyboardButton(
        text='Кнопка',
        callback_data='button_pressed'
    )
    # Создаем обьект инлайн-клавиатуры
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    # Отправляем сообщение пользователю
    await message.answer(text=LEXICON_RU['/start'], reply_markup=markup)
    logger.debug('Выходим из хендлера, обрабатывающего команду /start')


# Это хендлер, который мог бы обрабатывать любой текст,
# но 'MyFalseFilter' его не пропустит
@user_router.message(F.text, MyFalseFilter())
async def process_text(message: Message):
    logger.debug('Вошли в хендлер, обрабатывающий текст')
    logger.debug('Выходим из хендлера, обрабатывающего текст')
