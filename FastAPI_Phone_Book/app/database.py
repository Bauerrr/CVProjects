"""
File for creating database with given options.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use sqlite as database engine and save database to app.db file
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# Create sqlalchemy engine with given database url
# check_same_thread: False allows multithreading as multiple FastAPI functions could interact with db for the same request
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Instances of SessionLocal will be actual database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base for ORM models in models.py
Base = declarative_base()