from fastapi import FastAPI
from pydantic import BaseModel
from typing import List



class Users(BaseModel):
    name: str 
    age: int | None = None
    email: str| None = None
    password: str None = None
    active: bool | None = True

users = []
app =  FastAPI(
title = 'FAST API LMS',
description = "learning Management System for students",
version = "0.0.1",
terms_of_service = "http://example.com/terms/", 
contact={
"name": "Prince Owen",
"url" : 'https://www.linkedin.com/in/prince-owen-0b1a0a1a4/',
"email": "princeowen90@gmail.com" ,
},
license_info={
"name": "MIT License",
"url": "https://opensource.org/licenses/MIT",
},
tags_metadata=[
{ 
"name": "users",
"description": "users endpoints",
},
{   
"name": "courses",  
"description": "courses endpoints",
},
{
"name": "lessons",
"description": "lessons endpoints",
},
]
)



@app.get("/users", response_model=List[Users])
def get_users():
    return users

@app.post("/users")
def create_user(user: Users) -> dict:
    users.append(user.dict())
    return {"User created": user.dict()}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users[user_id]









