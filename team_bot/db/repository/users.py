import pickle

from team_bot.config import config
from team_bot.redis import redis_conn
from team_bot.db.session import async_session
from team_bot.db.models import Users, Projects

from sqlalchemy.future import select


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
                await session.refresh(user_data)
                await redis_conn.set(f'user:{user_data.telegram_id}', pickle.dumps(user_data))
                return True
            except Exception as e:
                print(e)
                return False
            
            
    async def check_user(self, user_id: int) -> bool:
        cached_user = await redis_conn.get(f'user:{user_id}')
        if cached_user:
            return True
        else:
            async with async_session() as session:
                user_data = session.execute(
                    select(Users).where(Users.telegram_id == user_id)
                )
                if user_data:
                    return True
                else:
                    return False
                
                
            
        
            
                
            
            
        
