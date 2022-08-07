#!/usr/bin/python3

import uuid
from datetime import datetime
import models
from xmlrpc.client import _iso8601_format


class BaseModel:
    """BaseModel defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                """created_at && updated_at converted to ISO format string"""
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
            models.storage.new(self)
        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """prints strings"""
        return ('[{}] ({}) {}'.format
                (self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
