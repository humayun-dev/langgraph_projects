# database models/tables
from sqlalchemy import Column, Integer, String, Float
from .connection import Base

# table object mapper
class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product = Column(String)
    city = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    