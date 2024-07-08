from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from ..database import Base
from ..main import app
from fastapi.testclient import TestClient
from fastapi import status
import pytest
from ..models import Todos, Users
from ..routers.auth import bcrpt_context

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/TodoApplicationTestDatabase'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'username': 'erictest', 'id': 1, 'user_role': 'admin'}


client = TestClient(app)
    

@pytest.fixture
def test_todo():
    todo= Todos(
        title="learn to code",
        description="need to do it",
        priority=5,
        complete=False,
        owner_id=1,
    )

    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.execute(text("ALTER SEQUENCE todos_id_seq RESTART WITH 1;"))
        connection.commit()


@pytest.fixture
def test_user():
    user = Users(
        username="erictest",
        email="erictest@email.com",
        first_name="eric",
        last_name="test",
        hashed_password=bcrpt_context.hash("testpassword"),
        role="admin",
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.execute(text("ALTER SEQUENCE users_id_seq RESTART WITH 1;"))
        connection.commit()