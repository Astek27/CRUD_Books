from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Book, UsersBooks

def get_users_books(db: Session, user_id: int) -> list[Book]:
    books_ids = db.query(UsersBooks).filter(UsersBooks.user_id == user_id).all()
    books_ids = [book.book_id for book in books_ids]
    users_books = [db.query(Book).filter(Book.id == book_id).scalar() for book_id in books_ids]
    return users_books


def add_book_for_user(db: Session, user_id: int, book_id: int) -> UsersBooks:
    book = db.query(UsersBooks).filter(
        UsersBooks.user_id == user_id,
        UsersBooks.book_id == book_id
    ).scalar()
    if book:
        return HTTPException(status_code=400, detail="Book already added for user")
    new_user_book = UsersBooks(user_id=user_id, book_id=book_id)
    db.add(new_user_book)
    return new_user_book