from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas import UserResponse

import app.repository.users as users_repo


def add_user(session: Session, login: str) -> UserResponse:
    if users_repo.get_user(session, login) is not None:
        raise HTTPException(status_code=400, detail="User already exist")
    user = users_repo.create_user(session, login)
    session.commit()
    return UserResponse.model_validate(user)