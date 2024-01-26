from sqlalchemy import(
    Column, Integer, BigInteger, 
    String, ForeignKey
)

from sqlalchemy.orm import DeclarativeBase, Relationship


Base = DeclarativeBase()


class Users(Base):
    __tablename__ = 'users'
    
    id = Column(BigInteger, primary_key=True)
    telegram_id = Column(Integer, unique=True,)
    nickname = Column(String(32), unique=True)
    lang = Column(String(6), nullable=False)
    
    projects = Relationship('Projects', back_populates='owner_id', lazy='selectin')
    
    
    
class Projects(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    owner_id = Column(BigInteger, ForeignKey('users.telegram_id'))
    name = Column(String(16), nullable=False)
    description = Column(String(50), nullable=False, default='None')
    
    owner = Relationship('Users', foreign_keys=[owner_id], lazy='selectin')
    
    

    
    
    
