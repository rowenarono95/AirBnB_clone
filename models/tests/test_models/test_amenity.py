#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.amenity_test = Amenity()
        cls.amenity_test.name = "test_class"

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity_test.__class__,
                        BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.amenity_test.__dict__)
        self.assertTrue('created_at' in self.amenity_test.__dict__)
        self.assertTrue('updated_at' in self.amenity_test.__dict__)
        self.assertTrue('name' in self.amenity_test.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.amenity_test.name), str)

    def test_save(self):
        self.amenity_test.save()
        self.assertNotEqual(self.amenity_test.created_at,
                            self.amenity_test.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.amenity_test), True)


if __name__ == "__main__":
    unittest.main()
