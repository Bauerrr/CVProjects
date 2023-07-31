"""
File with database models for ORM with SQLite.
"""
from sqlalchemy import Column, Integer, String

from .database import Base

class Contact(Base):
    __tablename__ = "contacts"

    contact_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)
    # Phone number as string for special cases like American free phone numbers or for adding country codes etc.
    phone_number = Column(String)
    email_address = Column(String)

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)