#!/usr/bin/python3
"""File Storage"""
from models.base_model import BaseModel
import json
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Class that serializes instances and deserializes JSON file"""

    __file_path = 'file.json'
    __objects = {}

    classes_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State
    }

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file with __file_path"""
        json_dict = {}

        for key, obj in FileStorage.__objects.items():
            json_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
            for key, value in json_dict.items():
                value = FileStorage.classes_dict[value['__class__']](value)
                FileStorage.__objects[key] = value
        except FileNotFoundError:
            pass
