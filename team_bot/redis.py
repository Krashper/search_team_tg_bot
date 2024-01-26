from redis.asyncio import Redis
from team_bot.config import config

redis_conn = Redis.from_url(config.REDIS_URL.unicode_string(), auto_close_connection_pool=True)
