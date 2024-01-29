from fastapi import FastAPI,Path,Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

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

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_all_books(book_id: int = Path(gt=0)):
    # for book in BOOKS:
    #     if book.id == book_id:
    #         return book
    return next(book for book in BOOKS if book.id == book_id)
    raise HTTPException(status_code=404, detail='Item not found')

@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    # book_to_return = []
    # for i in range(len(BOOKS)):
    #     if BOOKS[i].rating == book_rating:
    #         book_to_return.append (BOOKS[i])

    return list(book for book in BOOKS if book.rating == book_rating)


@app.post("/books/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(request_book: BookRequest):
    new_book = Book(**request_book.dict())
    BOOKS.append(find_book_id(new_book))


@app.put("/books/update_book/")
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            updated_book = Book(**book.dict())
            BOOKS[i] = updated_book
            book_chanegd = True
    if not book_changed:
        raise HTTPException(status_code=404, detail = 'Item not found')

@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')
def find_book_id(book: Book):
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book