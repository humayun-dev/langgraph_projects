# database connection with the Postgresql

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv

# load the database url
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)  # connects to postgres

# database sessions
SessionLocal = sessionmaker(
    autoflush = False,
    autocommit = False,
    bind = engine
)

# base class for all the models/tables
Base = declarative_base()