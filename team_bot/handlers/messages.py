from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


router = Router(name='messages')


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(message.text)
    
    
@router.message()
async def cmd_start(message: Message):
    await message.reply(message.text)


