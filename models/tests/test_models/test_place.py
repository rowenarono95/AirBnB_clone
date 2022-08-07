#!/usr/bin/python3
"""
Unittest for Place class
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.placeT = Place()
        cls.placeT.city_id = "Somewhere in India"
        cls.placeT.user_id = "Aladdin"
        cls.placeT.name = "Taj Mahal"
        cls.placeT.description = "Fit for a king"
        cls.placeT.number_rooms = 0
        cls.placeT.number_bathrooms = 0
        cls.placeT.max_guest = 0
        cls.placeT.price_by_night = 0
        cls.placeT.latitude = 0.0
        cls.placeT.longitude = 0.0
        cls.placeT.amenity_ids = []

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.placeT.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Place.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.placeT.__dict__)
        self.assertTrue('created_at' in self.placeT.__dict__)
        self.assertTrue('updated_at' in self.placeT.__dict__)
        self.assertTrue('city_id' in self.placeT.__dict__)
        self.assertTrue('user_id' in self.placeT.__dict__)
        self.assertTrue('name' in self.placeT.__dict__)
        self.assertTrue('description' in self.placeT.__dict__)
        self.assertTrue('number_rooms' in self.placeT.__dict__)
        self.assertTrue('number_bathrooms' in self.placeT.__dict__)
        self.assertTrue('max_guest' in self.placeT.__dict__)
        self.assertTrue('price_by_night' in self.placeT.__dict__)
        self.assertTrue('latitude' in self.placeT.__dict__)
        self.assertTrue('longitude' in self.placeT.__dict__)
        self.assertTrue('amenity_ids' in self.placeT.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.placeT.city_id), str)
        self.assertEqual(type(self.placeT.user_id), str)
        self.assertEqual(type(self.placeT.name), str)
        self.assertEqual(type(self.placeT.description), str)
        self.assertEqual(type(self.placeT.number_rooms), int)
        self.assertEqual(type(self.placeT.number_bathrooms), int)
        self.assertEqual(type(self.placeT.max_guest), int)
        self.assertEqual(type(self.placeT.price_by_night), int)
        self.assertEqual(type(self.placeT.latitude), float)
        self.assertEqual(type(self.placeT.longitude), float)
        self.assertEqual(type(self.placeT.amenity_ids), list)

    def test_save(self):
        self.placeT.save()
        self.assertNotEqual(self.placeT.created_at, self.placeT.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.placeT), True)


if __name__ == "__main__":
    unittest.main()
