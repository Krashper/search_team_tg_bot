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
    role = Column(String(16), name=False, default='user')
    status = Column(String(16), nullable=False, default='active')
    projects = Relationship("Projects", back_populates="owner", lazy='selectin')
    
    
class Projects(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    description = Column(String(50), nullable=False, default='None')
    owner = Column(BigInteger, ForeignKey('users.telegram_id'))
    users = 
    
    
