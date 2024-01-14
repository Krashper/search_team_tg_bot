from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_lang_kb(buttons: list[str]) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    for button in buttons:
        kb_builder.row(
            InlineKeyboardButton(
                text=button,
                callback_data=button
            )
        )
    return kb_builder.as_markup()

