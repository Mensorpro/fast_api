import fastapi
from pydantic import BaseModel
from typing import List
from api.utils.users import get_users, create_user, get_user

from db.db_setup import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from pydantic_schemas.user import UserCreate, User

router = fastapi.APIRouter()


@ router.get("/users", response_model=List[User], tags=["users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@ router.post("/users", response_model=User, tags=["users"])
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user





