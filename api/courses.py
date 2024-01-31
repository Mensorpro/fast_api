import fastapi


router = fastapi.APIRouter()

@router.get("/courses", tags=["courses"])
def get_courses():
    return {"courses": "courses"}

@router.post("/courses", tags=["courses"])
def create_courses():
    return {"courses": "courses"}

@router.get("/courses/{course_id}", tags=["courses"])
def get_course(course_id: int):
    return {"courses": "courses"}

@router.patch("/courses/{course_id}", tags=["courses"])
def update_course(course_id: int):
    return {"courses": "courses"}

@router.delete("/courses/{course_id}", tags=["courses"])
def delete_course(course_id: int):
    return {"courses": "courses"}
