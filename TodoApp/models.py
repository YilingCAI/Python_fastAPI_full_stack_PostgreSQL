from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default = True)
    role = Column(String)


class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(String)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))



""" create table Users(
    id Integer,
    email varchar(20) UNIQUE, 
    username varchar(20) UNIQUE, 
    first_name varchar(20), 
    last_name varchar(20), 
    hashed_password varchar(20), 
    is_active boolean default True, 
    role varchar(20),
	PRIMARY KEY(id)
	);


create table Todos(
    id Integer,
    title varchar(20), 
    description varchar(20), 
    priority integer, 
    complete varchar(20), 
    owner_id integer,
	PRIMARY KEY(id),
	CONSTRAINT fk_users
      FOREIGN KEY(owner_id) 
        REFERENCES users(id)
	); """