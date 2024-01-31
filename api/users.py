import fastapi
from pydantic import BaseModel
from typing import List

router = fastapi.APIRouter()


class Users(BaseModel):
    name: str 
    age: int
    email: str| None = None
    password: str 
    active: bool | None = True


users = []

@router.get("/users", response_model=List[Users], tags=["users"])
def get_users():
    return users

@router.post("/users", response_model=Users, tags=["users"])
def create_user(user: Users) -> dict:
    users.append(user.dict())
    return {"User created": user.dict()}

@router.get("/users/{user_id}", response_model=Users, tags=["users"])
def get_user(user_id: int):
    return users[user_id]





