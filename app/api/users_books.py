from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependency import get_current_user, get_db

from app.schemas import BookResponse
import app.service.users_books as users_books_serv

router = APIRouter()


@router.get('/my_books', response_model=list[BookResponse])
def get_my_books(db: Session = Depends(get_db),
                 current_user = Depends(get_current_user)):
    return users_books_serv.get_users_books(db, current_user)


@router.post('/add_book/{book_id}', response_model=BookResponse)
def add_book_for_user(book_id: int, db: Session = Depends(get_db),
                      current_user = Depends(get_current_user)):
    return users_books_serv.add_book_for_user(db, current_user, book_id)