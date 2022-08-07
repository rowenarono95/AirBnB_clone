#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.city_test = City()
        cls.city_test.name = "Aibonito"
        cls.city_test.state_id = "PR"

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.city_test.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.city_test.__dict__)
        self.assertTrue('created_at' in self.city_test.__dict__)
        self.assertTrue('updated_at' in self.city_test.__dict__)
        self.assertTrue('state_id' in self.city_test.__dict__)
        self.assertTrue('name' in self.city_test.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.city_test.name), str)
        self.assertEqual(type(self.city_test.state_id), str)

    def test_save(self):
        self.city_test.save()
        self.assertNotEqual(self.city_test.created_at,
                            self.city_test.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.city_test), True)


if __name__ == "__main__":
    unittest.main()
