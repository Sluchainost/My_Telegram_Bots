from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import game_kb, yes_no_kb, inline_kb
from lexicon.lexicon_ru import LEXICON_RU, LEXICON_INLINE_BUTTON_RU
from services.services import get_bot_choice, get_winner

router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


# Этот хэндлер срабатывает на отказ пользователя играть в игру
@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'], reply_markup=yes_no_kb)


stat_game: dict[str, int] = {
    'win_cnt': 0,
    'lose_cnt': 0,
    'draw_cnt': 0
}


# Этот хэндлер срабатывает на любую из игровых кнопок
@router.message(F.text.in_([LEXICON_RU['rock'],
                            LEXICON_RU['paper'],
                            LEXICON_RU['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    if winner == 'user_won':
        stat_game['win_cnt'] += 1
    elif winner == 'bot_won':
        stat_game['lose_cnt'] += 1
    else:
        stat_game['draw_cnt'] += 1
    await message.answer(
        text=f'{LEXICON_RU[winner]}\n'
        f'🟢Победа - {stat_game['win_cnt']}🟢\n'
        f'🔴Поражение - {stat_game['lose_cnt']}🔴\n'
        f'🟡Ничья - {stat_game['draw_cnt']}🟡\n\n'
        f'⚜Всего игр сыграно: {sum([value for value in stat_game.values()])}⚜',
        reply_markup=yes_no_kb
        )


# Этот хэндлер будет срабатывать на команду "/inline"
# и отправлять в чат клавиатуру с инлайн-кнопками
@router.message(Command(commands='inline'))
async def process_inline_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки. Нажми на любую!',
        reply_markup=inline_kb
        )


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@router.callback_query(F.data == [k for k in LEXICON_INLINE_BUTTON_RU.keys()][0])
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != [v for v in LEXICON_INLINE_BUTTON_RU.values()][0]:
        await callback.message.edit_text(
            text=[v for v in LEXICON_INLINE_BUTTON_RU.values()][0],
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='НАЖАТА КНОПКА НОМЕР 1')


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@router.callback_query(F.data == [k for k in LEXICON_INLINE_BUTTON_RU.keys()][1])
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != [k for k in LEXICON_INLINE_BUTTON_RU.values()][1]:
        await callback.message.edit_text(
            text=[v for v in LEXICON_INLINE_BUTTON_RU.values()][1],
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='НАЖАТА КНОПКА НОМЕР 2')


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@router.callback_query(F.data == [k for k in LEXICON_INLINE_BUTTON_RU.keys()][2])
async def process_button_3_press(callback: CallbackQuery):
    if callback.message.text != [k for k in LEXICON_INLINE_BUTTON_RU.values()][2]:
        await callback.message.edit_text(
            text=[v for v in LEXICON_INLINE_BUTTON_RU.values()][2],
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='НАЖАТА КНОПКА НОМЕР 3')


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@router.callback_query(F.data == [k for k in LEXICON_INLINE_BUTTON_RU.keys()][3])
async def process_button_4_press(callback: CallbackQuery):
    if callback.message.text != [k for k in LEXICON_INLINE_BUTTON_RU.values()][3]:
        await callback.message.edit_text(
            text=[v for v in LEXICON_INLINE_BUTTON_RU.values()][3],
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(
        text='НАЖАТА КНОПКА НОМЕР 4',
        show_alert=True)
