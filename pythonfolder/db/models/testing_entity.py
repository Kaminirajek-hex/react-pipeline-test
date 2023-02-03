from sqlalchemy import Boolean, Column, Float, Integer, String
from db.base import Base


class Testing_entity(Base):
    __tablename__ = "Testing_entity"
    id = Column(Integer, primary_key=True)
    
    name = Column(String(50), nullable=False)
    number = Column(Integer, nullable=False)