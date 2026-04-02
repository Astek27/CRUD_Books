from fastapi import FastAPI
from app.api.books import router as books_router
from app.api.users import router as users_router
from app.database import Base, engine

app = FastAPI()

app.include_router(books_router, prefix='/api/books', tags=['books'])
app.include_router(users_router, prefix='/api/users', tags=['users'])

Base.metadata.create_all(bind=engine)