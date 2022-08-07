#!/usr/bin/python3
"""Module place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Contains class attr:
        city_id, user_id, name,
        description, numer_rooms,
        numbr_bathrooms, max_guest,
        price_by_night, latitude,
        longitude, amenity_ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
