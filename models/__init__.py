#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.place import Place
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
