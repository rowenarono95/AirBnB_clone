#!/usr/bin/python3
"""
Unittest for console command interpreter
"""
import unittest
from unittest.mock import patch
from io import StringIO
import json
import console
import tests
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):

    """Unittest for command interpreter"""
    @classmethod
    def setUpClass(self):
        """Set up test"""
        self.typing = console.HBNBCommand()

    def test_docstrings_in_test_console(self):
        """Test docstrings exist in test_console.py"""
        self.assertTrue(len(self.__doc__) >= 1)

    def test_create(self):
        """Test cmd output: create"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create Non")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

    def test_all(self):
        """Test cmd output: all"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("all Non")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

    def test_destroy(self):
        """Test cmd output: destroy"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy Country")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy City")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy City 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())

    def test_update(self):
        """Test cmd output: update"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update Non")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update User")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())

    def test_show(self):
        """Test cmd output: show"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("show City")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())


if __name__ == "__main__":
    unittest.main()
