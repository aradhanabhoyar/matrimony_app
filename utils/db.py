from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    "sqlite:///matrimony.db",
    connect_args={"check_same_thread": False}  
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    from models.user_model import User
    from models.profile_model import Profile

    Base.metadata.create_all(bind=engine)