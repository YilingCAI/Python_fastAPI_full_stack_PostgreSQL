from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
import models 
from models import Todos
from database import SessionLocal
from starlette import status
from pydantic import BaseModel, Field
from models import Users
from passlib.context import CryptContext

router = APIRouter()

bcrpt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class CreateUserRequest(BaseModel): 
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str


@router.post("/auth/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, 
                      create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password=bcrpt_context.hash(create_user_request.password),
        role=create_user_request.role,
        is_active=True

    )

    db.add(create_user_model)
    db.commit()


@router.get("/auth/")
async def get_user():
    return {'user': 'authenticated'}