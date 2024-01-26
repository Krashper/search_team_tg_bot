from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.strategy import FSMStrategy

from team_bot.config import config
from team_bot.handlers import messages


async def main():
    bot = Bot(token=config.TOKEN)
    storage = RedisStorage.from_url(config.REDIS_URL.unicode_string(), )
    dp = Dispatcher(storage=storage, fsm_strategy=FSMStrategy.USER_IN_CHAT)
    
    # подключение роутеров
    dp.include_router(messages.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
