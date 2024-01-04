# CRUD
from fastapi import FastAPI, Body

# uvicorn books:app --reload
# uvicorn books:app --reload

app = FastAPI()  # uvicorn is the web server for starting an application

BOOKS = [
    {"title": "Title One", "Author": "Author One", "Category": "Science"},
    {'title': 'Title Two', 'Author': 'Author Two', 'Category': 'Science'},
    {'title': 'Title Three', 'Author': 'Author Three', 'Category': 'history'},
    {'title': 'Title Four', 'Author': 'Author Four', 'Category': 'math'},
    {'title': 'Tneitle Five', 'Author': 'Author Fie', 'Category': 'math'},
    {'title': 'Title Six', 'Author': 'Author Six', 'Category': 'math'}
]


# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param):
#     return {'dynamic_params': {dynamic_param}}

# @app.get("/books/{book_title}")
# async def read_all_books(book_title: str):
#     for book in BOOKS:
#         if book.get('title').casefold() == book_title.casefold():
#             return book


# query parameter  ?key=value
@app.get("/books/{book_author}")
async def read_author_category_by_query_book(book_author: str, category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('Author').casefold() == book_author.casefold() and book.get(
                'Category').casefold() == category.casefold():
            book_to_return.append(book)

    return book_to_return


@app.post("/books/create_books")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] == updated_book


@app.delete("/books/delete_books/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title:
            BOOKS.pop(i)
            break
