from fastapi import FastAPI
from api import users, courses, sections
from db.db_setup import engine
from db.models import course, user


user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

#trying to make a change



app =  FastAPI(
title = 'FAST API LMS',
description = "Learning Management System for Students",
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


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)









