import asyncio
import logging




# Start the bot
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(TOKEN=TOKEN))