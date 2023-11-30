#!/usr/bin/python3
"""This module defines a class User"""
from .base_model import BaseModel, Base
from sqlalchemy import Column, String



class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
