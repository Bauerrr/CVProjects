"""
File with pydantic schemas for database models. Used mainly for data validation, before database insertion.
"""

from pydantic import BaseModel, EmailStr


class ContactBase(BaseModel):
    name: str
    last_name: str
    phone_number: str
    email_address: EmailStr

class Contact(ContactBase):
    contact_id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserBase(BaseModel):
    username: str
    password: str

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True
