from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependency import get_db
from app.schemas import CreateUser, UserResponse
import app.service.users as users_serv


router = APIRouter()


@router.post('/create', response_model=UserResponse)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    return users_serv.add_user(session=db, login=user.login)
