#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import Base
from models.city import City
from models.state import State
from sqlalchemy import Column


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id_exists(self):
        """ """
        self.assertTrue(hasattr(self.value, 'state_id'))

    def test_name_exists(self):
        """ """
        self.assertTrue(hasattr(self.value, 'name'))

    # def test_inherits_from_Base(self):
    #     """ """
    #     state = State(name="Niger")
    #     new = self.value(name="Minna", state_id=state.id)
    #     self.assertIsInstance(new, Base)
