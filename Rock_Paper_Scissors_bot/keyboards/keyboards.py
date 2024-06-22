from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU, LEXICON_INLINE_BUTTON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# ------- Создаем игровую клавиатуру без использования билдера -------

# Создаем кнопки игровой клавиатуры
button_1 = KeyboardButton(text=LEXICON_RU['rock'])
button_2 = KeyboardButton(text=LEXICON_RU['scissors'])
button_3 = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3]],
    resize_keyboard=True
)

# ------- Создаем инлайн клавиатуру -------

# Создаем объекты инлайн-кнопок
big_button_1 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data=[k for k in LEXICON_INLINE_BUTTON_RU.keys()][0]
)

big_button_2 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data=[k for k in LEXICON_INLINE_BUTTON_RU.keys()][1]
)

big_button_3 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 3',
    callback_data=[k for k in LEXICON_INLINE_BUTTON_RU.keys()][2]
)

big_button_4 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 4',
    callback_data=[k for k in LEXICON_INLINE_BUTTON_RU.keys()][3]
)

# Создаем объект инлайн-клавиатуры
inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1], [big_button_2],
                     [big_button_3], [big_button_4]]
)
