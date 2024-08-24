import logging

from aiogram import Router
from aiogram.types import Message
from filters.filters import MyTrueFilter
from lexicon.lexicon import LEXICON_RU


logger = logging.getLogger(__name__)

# Инициализируем роутер уровня модуля
other_router = Router()


# Этот хендлер будет срабатыватьна любые сообщения,
# кроме тех, для которых есть отдельные хендлеры
@other_router.message(MyTrueFilter())
async def send_echo(message: Message):
    logger.debug('Вошли в эхо-хендлер')
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
    logger.debug('Выходим из эхо-хендлера')
