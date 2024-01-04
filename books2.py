from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

BOOKS = []


class Book:
    id: int = 0
    tilte: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(title="id is not needed")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=200)
    rating: int = Field(gt=-1, lt=6)

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'a new book',
                'author': 'mimi',
                'description': 'dees',
                'rating': 5
            }
        }


BOOKS = [
    Book(1, 'CS Pro', 'mimi', 'good book', 5),
    Book(2, 'CS Pro 1', 'mimi', 'good book 4', 2),
    Book(3, 'CS Pro 1', 'mimi', 'good book 3', 3),
    Book(4, 'HP1', 'mimi 3', 'good book 5', 4),
    Book(5, 'HP2', 'mimi 4', 'good book 4', 5),
    Book(6, 'HP3', 'mimi 5', 'good book 5', 1)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/books/create_book")
async def create_book(request_book: BookRequest):
    new_book = Book(**request_book.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book