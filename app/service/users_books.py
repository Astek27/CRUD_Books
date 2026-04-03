from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Book, User
from app.schemas import BookResponse

import app.repository.users_books as users_books_repo
import app.repository.books as books_repo


def get_users_books(db: Session, current_user: User) -> list[BookResponse]:
    books = users_books_repo.get_users_books(db, current_user.id)
    books = [BookResponse.model_validate(book) for book in books]
    return books


def add_book_for_user(db: Session, current_user: User, book_id: int) -> BookResponse:
    book = books_repo.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    users_books_repo.add_book_for_user(db, current_user.id, book_id)
    db.commit()
    return BookResponse.model_validate(book)