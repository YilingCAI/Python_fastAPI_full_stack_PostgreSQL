# CRUD
from fastapi import FastAPI

# uvicorn boooks:app --reload

app = FastAPI()  # uvicorn is the web server for starting an application

BOOKS = [
    {'title':'Title One', 'Author': 'Arthur One', 'Category': 'Science'},
{'title':'Title Two', 'Author': 'Arthur Two', 'Category': 'Science'},
{'title':'Title Three', 'Author': 'Arthur Three', 'Category': 'history'},
{'title':'Title Four', 'Author': 'Arthur Four', 'Category': 'math'},
{'title':'Tneitle Five', 'Author': 'Arthur Fie', 'Category': 'math'},
{'title':'Title Six', 'Author': 'Arthur Six', 'Category': 'math'}
]


# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param):
#     return {'dynamic_params': {dynamic_param}}

@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book