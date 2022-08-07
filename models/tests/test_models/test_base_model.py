#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_test = BaseModel()
        cls.base_test.name = "Gabriel"
        cls.base_test.my_number = 26

    def test_checking_for_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        self.assertTrue(isinstance(self.base_test, BaseModel))

    def test_save(self):
        self.base_test.save()
        self.assertNotEqual(self.base_test.created_at,
                            self.base_test.updated_at)

    def test_to_dict(self):
        base_test_dict = self.base_test.to_dict()
        self.assertEqual(self.base_test.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_test_dict['created_at'], str)
        self.assertIsInstance(base_test_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
