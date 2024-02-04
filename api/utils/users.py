from sqlalchemy.orm import Session
from db.models.user import User
from pydantic_schemas.user import UserCreate    


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, password=user.password, username=user.username,role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
    
def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()

def delete_user(db: Session, user_id: int):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return {"User deleted": user_id}

def update_user(db: Session, user_id: int, user: UserCreate):
    db.query(User).filter(User.id == user_id).update(user.dict())
    db.commit()
    return {"User updated": user_id}

def deactivate_user(db: Session, user_id: int):
    db.query(User).filter(User.id == user_id).update({"is_active": False})
    db.commit()
    return {"User deactivated": user_id}

def activate_user(db: Session, user_id: int):
    db.query(User).filter(User.id == user_id).update({"is_active": True})
    db.commit()
    return {"User activated": user_id}

def get_active_users(db: Session):
    return db.query(User).filter(User.is_active == True).all()

def get_inactive_users(db: Session):
    return db.query(User).filter(User.is_active == False).all()



