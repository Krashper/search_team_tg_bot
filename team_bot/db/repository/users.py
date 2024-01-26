import pickle

from team_bot.config import config
from team_bot.redis import redis_conn
from team_bot.db.session import async_session
from team_bot.db.models import Users, Projects


class UserRepositoryInterface:
    async def add_user(self, user_data: Users) -> bool:
        pass
    
    async def add_project(self, project_data: Projects) ->bool:
        pass
    
    
class UserRepository(UserRepositoryInterface):
    def __init__(self) -> None:
        ...
        
    
    async def add_user(self, user_data: Users) -> bool:
        async with async_session() as session:
            try:
                await session.add(user_data)
                await session.commit()
                return True
            except Exception as e:
                print(e)
                return False
            
                
            
            
        
