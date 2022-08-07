#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.revT = Review()
        cls.revT.place_id = "Santurce"
        cls.revT.user_id = "Gabriel"
        cls.revT.text = "Five Stars"

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.revT.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.revT.__dict__)
        self.assertTrue('created_at' in self.revT.__dict__)
        self.assertTrue('updated_at' in self.revT.__dict__)
        self.assertTrue('place_id' in self.revT.__dict__)
        self.assertTrue('text' in self.revT.__dict__)
        self.assertTrue('user_id' in self.revT.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.revT.text), str)
        self.assertEqual(type(self.revT.place_id), str)
        self.assertEqual(type(self.revT.user_id), str)

    def test_save(self):
        self.revT.save()
        self.assertNotEqual(self.revT.created_at, self.revT.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.revT), True)


if __name__ == "__main__":
    unittest.main()
