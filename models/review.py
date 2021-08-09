#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy.sql.functions import user
from models import place
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class Review(BaseModel):
    """ Review class to store review information """
    __tablename__ = "reviews"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        place_id = Column(String(60), nullable=False)
        user_id = Column(String(60), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
