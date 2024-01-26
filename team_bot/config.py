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
    
    @field_validator('REDIS_URL')
    def redis_url(cls, v: Optional[str], values: Dict[str, Any]):
        if isinstance(v, str):
            return v
        return RedisDsn.build(
            scheme='redis',
            password=values.data.get('REDIS_PASSWORD'),
            host=values.data.get('REDIS_SERVER'), 
            port=int(values.data.get('REDIS_PORT')),
            path=values.data.get('REDIS_DB'), 
        )
    
    # PostgreSQL
    POSTGRES_DRV: str
    POSTGRES_DRV_FOR_MIGRATIONS: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD:str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    SQLALCHEMY_DB_URL: Optional[PostgresDsn] = None
    
    @field_validator('SQLALCHEMY_DB_URL')
    def alchemy_url(cls, v: Optional[str], values: Dict[str, Any]):
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme=values.data.get('POSTGRES_DRV'),
            username=values.data.get('POSTGRES_USER'),
            password=values.data.get('POSTGRES_PASSWORD'),
            host=values.data.get('POSTGRES_SERVER'),
            port=int(values.data.get('POSTGRES_PORT'),),
            path=f"{values.data.get('POSTGRES_DB')}"
        )
    SQLALCHEMY_DB_URL_FOR_MIGRATIONS: Optional[PostgresDsn] = None
    
    @field_validator('SQLALCHEMY_DB_URL_FOR_MIGRATIONS')
    def alchemy_url_for_migrations(cls, v: Optional[str], values: Dict[str, Any]):
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme=values.data.get('POSTGRES_DRV_FOR_MIGRATIONS'),
            username=values.data.get('POSTGRES_USER'),
            password=values.data.get('POSTGRES_PASSWORD'),
            host=values.data.get('POSTGRES_SERVER'),
            port=int(values.data.get('POSTGRES_PORT'),),
            path=f"{values.data.get('POSTGRES_DB')}"
        )
    
config = Config()
