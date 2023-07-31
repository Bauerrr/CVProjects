"""
File with JWT authentication functions.
"""
from datetime import datetime, timedelta
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from . import schemas, crud
from .database import SessionLocal

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

# Variables for generating token
SECRET_KEY = "b52c1fa330a2e6e53ee37ea164f1ae623dfaca7ace1bc8e1af6d69677bc048e1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def get_db():
    """Create database session for given operation and close session afterwards"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CryptContext for encrypting user password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User verification scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    """Hash password given by the user and compare it to the hashed password in database"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Get hashed password"""
    return pwd_context.hash(password)

def get_user(db: Session, username: str):
    """Return user data as JSON"""
    user = crud.read_user(db=db, username=username)
    if user:
        return schemas.User(user_id=user.user_id, username=user.username, password=user.password)
    
def authenticate_user(db: Session, username: str, password: str):
    """Check if users credentials are valid"""
    user = get_user(db=db, username=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Create acces token from user data, secret key and expiration date with given algorithm"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    """Decodes token and checks if user encoded in token exists. If user exists, returns user"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(db=db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user