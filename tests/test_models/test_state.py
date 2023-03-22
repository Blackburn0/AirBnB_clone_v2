#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import Base
from models.state import State
from sqlalchemy import Column


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3_exists(self):
        """ """
        self.assertTrue(hasattr(self.value, 'name'))

    def test_cities_exists(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(self.value, 'cities'))

    # def test_inherits_from_Base_class(self):
    #     """ """
    #     new = self.value()
    #     self.assertIsInstance(new, Base)
