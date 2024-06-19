from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
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
