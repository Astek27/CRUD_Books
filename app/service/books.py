from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Book
from app.schemas import BookResponse, CreateBook
import app.repository.books as books_repo


def add_book(db: Session, book: CreateBook) -> BookResponse:
    if books_repo.is_book_in_base(db, book.name, book.author):
        raise HTTPException(status_code=400, detail='This book already exist')
    book = books_repo.add_book(db, name=book.name, author=book.author)
    db.commit()
    return BookResponse.model_validate(book)


def get_all_books(db: Session) -> list[BookResponse]:
    books = books_repo.get_all_books(db)
    books = [BookResponse.model_validate(book) for book in books]
    return books