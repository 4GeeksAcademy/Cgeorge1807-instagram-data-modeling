import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250),nullable=False)
    lastname = Column(String(250),nullable=False)
    username = Column(String(250),nullable=False)


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    url_image = Column(String(250),nullable=False)
    likes = Column(Integer)
    description = Column(String(250))
    person_id = Column(Integer, ForeignKey('user.id'))
    person = relationship(User)

       
