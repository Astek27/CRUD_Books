from sqlalchemy.orm import Session

from app.models import Book


def is_book_in_base(db: Session, name: str, author: str) -> bool:
    return db.query(Book).filter(Book.name == name, Book.author == author).first() is not None


def add_book(db: Session, name: str, author: str) -> Book:
    book = Book(name=name, author=author)
    db.add(book)
    db.flush()
    return book


def get_all_books(db: Session) -> list[Book]:
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int) -> Book | None:
    return db.query(Book).filter(Book.id == book_id).first()

