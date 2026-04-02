from sqlalchemy.orm import Session

from app.models import User
from app.schemas import BookResponse

import app.repository.users_books as users_books_repo


def get_users_books(db: Session, current_user: User) -> list[BookResponse]:
    books = users_books_repo.get_users_books(db, current_user.id)
    books = [BookResponse.model_validate(book) for book in books]
    return books
