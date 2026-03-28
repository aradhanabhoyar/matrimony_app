from sqlalchemy import Column, Integer, String, ForeignKey
from utils.db import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    age = Column(Integer)
    gender = Column(String)
    religion = Column(String)
    city = Column(String)