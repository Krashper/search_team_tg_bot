from sqlalchemy import(
    Column, Integer, BigInteger, 
    String, Text, JSON
)

from sqlalchemy.orm import DeclarativeBase




Base = DeclarativeBase()


class Questions(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    question = Column(Text)
    description = Column(Text)