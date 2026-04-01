from fastapi import FastAPI
from app.api.books import router as books_router
from app.database import Base, engine

app = FastAPI()

app.include_router(books_router, prefix='/api/books', tags=['books'])

Base.metadata.create_all(bind=engine)