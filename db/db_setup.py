from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:Princeowen2002@localhost/Fast-api-sever"

engine = create_engine(SQLALCHEMY_DATABASE_URL,future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()




        
    

    

