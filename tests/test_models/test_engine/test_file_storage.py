#!/usr/bin/python3

""" Test File storage classes"""

from datetime import datetime
import inspect
import models
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os
import pep8
import unittest


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    def test_new(self):
        """test that new adds an object to the database"""

    def test_save(self):
        """Test that save properly saves objects to file.json"""

    def test_get(self):
        """Test that get returns specific object, or none"""
        newState = State(name="New York")
        newState.save()
        newUser = User(email="bob@foobar.com", password="password")
        newUser.save()
        self.assertIs(newState, models.storage.get("State", newState.id))
        self.assertIs(None, models.storage.get("State", "blah"))
        self.assertIs(None, models.storage.get("blah", "blah"))
        self.assertIs(newUser, models.storage.get("User", newUser.id))

    def test_count(self):
        """add new object to db"""
        startCount = models.storage.count()
        self.assertEqual(models.storage.count("Blah"), 0)
        newState = State(name="Montevideo")
        newState.save()
        newUser = User(email="ralexrivero@gmail.com.com", password="dummypass")
        newUser.save()
        self.assertEqual(models.storage.count("State"), startCount + 1)
        self.assertEqual(models.storage.count(), startCount + 2)

if __name__ == "__main__":
    unittest.main()
