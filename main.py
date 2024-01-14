import asyncio
import logging

from team_bot.bot import main
from config_data.config import load_config


# Start the bot
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    config = load_config()
    TOKEN = config.tg_bot.token
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(TOKEN=TOKEN))