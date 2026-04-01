from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependency import get_db
from app.schemas import BookResponse, CreateBook
import app.service.books as books_serv

router = APIRouter()


@router.post('/add', response_model=BookResponse)
def add_book(book: CreateBook, db: Session = Depends(get_db)):
    return books_serv.add_book(db, book)


@router.get('/', response_model=list[BookResponse])
def get_all_books(db: Session = Depends(get_db)):
    return books_serv.get_all_books(db)