import os
from pydantic_settings import BaseSettings
from typing import Any, Dict, List, Optional
from pydantic.functional_validators import field_validator
from pydantic import RedisDsn, PostgresDsn


if os.path.isfile('.env'):
    from dotenv import load_dotenv
    load_dotenv()
    print('Loading environment variables from .env')
else:
    print("No .env file found. Using system environment variables.")


class Config(BaseSettings):
    
    TOKEN: str

    # Redis validation
    REDIS_SERVER: str
    REDIS_PORT: str
    REDIS_DB: Optional[str] = None
    REDIS_PASSWORD: Optional[str] = None
    REDIS_URL: Optional[RedisDsn] = None
    
    # PostgreSQL
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD:str
    POSTGRES_DB: str
    SQLALCHEMY_DB_URL: Optional[PostgresDsn] = None
    
config = Config()
    
    
    

