from sqlalchemy.orm import Session

from app.models import Book, UsersBooks

def get_users_books(db: Session, user_id: int) -> list[Book]:
    books_ids = db.query(UsersBooks).filter(UsersBooks.user_id == user_id).all()
    books_ids = [book.book_id for book in books_ids]
    users_books = [db.query(Book).filter(Book.id == book_id).scalar() for book_id in books_ids]
    return users_books
