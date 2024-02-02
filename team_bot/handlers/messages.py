from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.state import State, StatesGroup, default_state
from team_bot.lexicon.lexicon import LEXICON
from aiogram.fsm.context import FSMContext
from team_bot.database.db import check_register, is_unique_name, create_new_user
from team_bot.keyboards.register_kb import create_lang_kb, create_get_username_kb

# import db models classes
from team_bot.db.models import Users

from team_bot.db.repository import UserRepository

user_data = Users()
user_repo = UserRepository()

languages = ['Русский', 'English']

class Register(StatesGroup):
    fill_username = State()
    fill_language = State()
    fill_name = State()
    fill_age = State()

router = Router(name='messages')


@router.message(CommandStart(), StateFilter(default_state))
async def cmd_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if await user_repo.check_user(user_id=user_id):
        await message.answer(text=LEXICON['/start'])
    else:
        await message.answer(
            text=LEXICON['select_lang'],
            reply_markup=create_lang_kb(languages)
        )
        await state.set_state(Register.fill_language)


@router.callback_query(F.data.in_(languages), StateFilter(Register.fill_language))
async def language_register(callback: CallbackQuery, state: FSMContext):
    await state.update_data(lang=callback.data)
    await callback.message.edit_text(
        text=LEXICON['get_username'],
        reply_markup=create_get_username_kb(['Разрешить'])
    )
    await state.set_state(Register.fill_username)

@router.callback_query(F.data.in_('Разрешить'), StateFilter(Register.fill_username))
async def username_register(callback: CallbackQuery, state: FSMContext):
    username = callback.from_user.username
    if username:
        await callback.message.edit_text(
            text=LEXICON['select_name']
        )
        await state.update_data(username=callback.from_user.username)
        await state.set_state(Register.fill_name)
    else:
        await callback.message.edit_text(
            text=LEXICON['username_none'],
            reply_markup=create_get_username_kb(['Разрешить'])
        )

@router.message(F.text.isalpha(), StateFilter(Register.fill_name))
async def name_register(message: Message, state: FSMContext):
    if is_unique_name(message.text):
        await state.update_data(name=message.text)
        await message.answer(
            text=LEXICON['select_age']
        )
        await state.set_state(Register.fill_age)
    else:
        await message.answer(
            text=LEXICON['non_unique_name']
        )

@router.message(StateFilter(Register.fill_name))
async def name_error(message: Message, state: FSMContext):
    await message.answer(
        text=LEXICON['non_valid_name']
    )

@router.message(F.text.isdigit(), lambda x: 10 <= int(x.text) <= 100, StateFilter(Register.fill_age))
async def age_register(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer(
        text=LEXICON['finish_register']
    )
    data = await state.get_data()
    user_data.id = -1
    user_data.telegram_id = message.from_user.id
    user_data.lang = data['lang']
    user_data.name = data['name']
    user_data.nickname = data['username'],
    user_data.age = data['age']       
    await user_repo.add_user(user_data=user_data)    
    await state.clear()

@router.message(StateFilter(Register.fill_age))
async def age_error(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(
            text=LEXICON['digit_age_error']
        )
    elif int(message.text) > 100:
        await message.answer(
            text=LEXICON['max_age_error']
        )
    else:
        await message.answer(
            text=LEXICON['min_age_error']
        )

@router.message(Command('menu'), StateFilter(default_state))
async def show_main_menu(message: Message, state: FSMContext):
    await message.answer(
        text='Главное меню'
    )