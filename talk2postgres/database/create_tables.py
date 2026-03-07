# to map the tables automatically to the postgres
from .connection import engine,Base
from . import models

def create_tables():
    Base.metadata.create_all(bind = engine)