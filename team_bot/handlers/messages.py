from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.state import State, StatesGroup, default_state
from team_bot.lexicon.lexicon import LEXICON
from aiogram.fsm.context import FSMContext
from team_bot.database.db import check_register
from team_bot.keyboards.register_kb import create_lang_kb

languages = ['Русский', 'English']

class Register(StatesGroup):
    fill_language = State()
    fill_name = State()
    fill_age = State()
    fill_phone = State()

router = Router(name='messages')

async def ask_for_telegram_link(message: Message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="Разрешить", url="https://t.me/KrashperFirst_bot?start=allow_contact")
    keyboard.add(button)
    await message.answer("Пожалуйста, разрешите боту получить вашу ссылку на Telegram, нажав на кнопку ниже.", reply_markup=keyboard)


@router.message(commands=['start'])
async def save_telegram_link(message: Message):
    if "allow_contact" in message.get_args():
        user_id = message.from_user.id
        username = message.from_user.username
        link = f"https://t.me/{username}"
        # Сохраняем ссылку в базе данных или другом хранилище
        await message.answer(f"Спасибо! Ваша ссылка на Telegram сохранена: {link}")
    else:
        await message.answer("Для продолжения работы с ботом, пожалуйста, разрешите ему получить вашу ссылку на Telegram.")


'''@router.message(CommandStart(), StateFilter(default_state))
async def cmd_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if check_register(user_id):
        await message.answer(text=LEXICON['/start'])
    else:
        await message.answer(
            text=LEXICON['select_lang'],
            reply_markup=create_lang_kb(languages)
        )
        await state.set_state(Register.fill_language)

@router.callback_query(F.data.in_(languages), StateFilter(Register.fill_language))
async def name_register(callback: CallbackQuery, state: FSMContext):
    await state.update_data(lang=callback.data)
    await callback.message.edit_text(
        text=LEXICON['select_name']
    )
    await state.set_state(Register.fill_name)

@router.message(F.text.isalpha(), StateFilter(Register.fill_name))
async def age_register(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        text=LEXICON['select_age']
    )
    await state.set_state(Register.fill_age)

@router.message(F.text.isdigit(), lambda x: 10 <= int(x) <= 100, StateFilter(Register.fill_age))
async def phone_register(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer(
        text=LEXICON['select_phone']
    )
    await state.set_state(Register.fill_phone)

@router.message(F.text.isalpha(), StateFilter(Register.fill_name))
async def age_register(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        text=LEXICON['select_age']
    )
    await state.set_state(Register.fill_age)'''

