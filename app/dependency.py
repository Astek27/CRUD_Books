from typing import Generator
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User
import app.repository.users as user_repo


security = HTTPBearer()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    login = credentials.credentials
    user = user_repo.get_user(db, login)
    if not user:
        raise HTTPException(status_code=401, detail='Not authorise')
    return user