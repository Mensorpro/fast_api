from ..db_setup import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum


class Role(enum.Enum):
    admin = 1
    user = 2




class User(Base):
    __tablename__ = 'users' 

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    password = Column(String(50), nullable=False,index=True)
    email = Column(String(50), nullable=False, unique=True, index=True)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(Role), default=Role.user)

    profile = relationship('Profile', back_populates='owner', uselist=False)

    def __repr__(self):
        return f'<User {self.username}>'
    

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='profile')
    first_name = Column(String(50), nullable=False, index=True)
    last_name = Column(String(50), nullable=False, index=True)
    phone = Column(Integer(), nullable=False, index=True)
    address = Column(String(50), nullable=False, index=True)
    city = Column(String(50), nullable=False, index=True)
    state = Column(String(50), nullable=False, index=True)
    zipcode = Column(Integer(), nullable=False, index=True) 
    bio = Column(String(50), nullable=False, index=True)


    owner = relationship('User', back_populates='profile')

    def __repr__(self):
        return f'<Profile {self.first_name} {self.last_name}>'
    

