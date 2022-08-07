#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stateT = State()
        cls.stateT.name = "Puerto_Rico"

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.stateT.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.stateT.__dict__)
        self.assertTrue('created_at' in self.stateT.__dict__)
        self.assertTrue('updated_at' in self.stateT.__dict__)
        self.assertTrue('name' in self.stateT.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.stateT.name), str)

    def test_save(self):
        self.stateT.save()
        self.assertNotEqual(self.stateT.created_at, self.stateT.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.stateT), True)


if __name__ == "__main__":
    unittest.main()
