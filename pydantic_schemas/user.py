from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str 
    role : str | None = "user"

class UserCreate(UserBase):
    password : str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime


    class Config:
        orm_mode = True

