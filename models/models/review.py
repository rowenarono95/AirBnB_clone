#!/usr/bin/python3
"""module review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Contains class attr"""

    place_id = ""
    user_id = ""
    text = ""
