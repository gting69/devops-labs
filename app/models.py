from sqlalchemy import Column, Integer, String
from .database import Base

class Cat(Base):
    __tablename__ = "battle_cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialty = Column(String)