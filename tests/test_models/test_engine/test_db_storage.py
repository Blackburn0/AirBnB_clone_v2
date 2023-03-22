"""Module for testing DB storage"""
import unittest
import os
from models import storage
from models.state import State

store_type = os.getenv('HBNB_TYPE_STORAGE')


@unittest.skipIf(store_type != 'db', 'Test for DBStorage')
class test_dbstorage(unittest.TestCase):
    """Class to test the DB storage method"""

    def setUp(self):
        """Sets up test db for testing"""
        pass

    def tearDown(self):
        """Tears Down test db after each test"""
        pass

    def test_all(self):
        """ """
        temp = storage.all(State)
        self.assertIsInstance(temp, dict)

    def test_new(self):
        """ """
        test = State(name="Niger")
        storage.new(test)
        self.assertTrue(len(storage.all(State).keys()) > 0)

    def test_save(self):
        """ """
        pass

    def test_delete(self):
        """ """
        test1 = State(name="Niger")
        test2 = State(name="FCT")
        test1.save()
        test2.save()
        key = test1.to_dict()['__class__'] + '.' + test1.id
        test1.delete()
        self.assertFalse(key in storage.all(State).keys())
