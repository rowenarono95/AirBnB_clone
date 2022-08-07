#!/usr/bin/python3
"""
    Test Case for state Model
"""
from models import BaseModel
from models import State
import unittest
import models


class Teststate(unittest.TestCase):
    """
        unitesst for state class
    """
    def issub_class(self):
        """
            test if state class is sub class of base model
        """
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "update_at"))

    def test_name_attr(self):
        """
            Test that State has attribute name
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def setUp(self):
        self.state = State()

    def test_state_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attr_is_a_class_attr(self):
        self.assertTrue(hasattr(self.state, "name"))

    def test_class_attrs(self):
        self.assertIs(type(self.state.name), str)
        self.assertFalse(bool(self.state.name))


if __name__ == "__main__":
    unittest.main()
