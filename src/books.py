# CRUD
from fastapi import FastAPI

# uvicorn boooks:app --reload

app = FastAPI()  # uvicorn is the web server for starting an application

@app.get("/")
async def first_api():
    return {'messages': "hello eric!"}

