#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        self.assertTrue(hasattr(self.value, 'city_id'))

    def test_user_id(self):
        """ """
        self.assertTrue(hasattr(self.value, 'user_id'))

    def test_name(self):
        """ """
        self.assertTrue(hasattr(self.value, 'name'))

    def test_description(self):
        """ """
        self.assertTrue(hasattr(self.value, 'description'))

    def test_number_rooms(self):
        """ """
        self.assertTrue(hasattr(self.value, 'number_rooms'))

    def test_number_bathrooms(self):
        """ """
        self.assertTrue(hasattr(self.value, 'number_bathrooms'))

    def test_max_guest(self):
        """ """
        self.assertTrue(hasattr(self.value, 'max_guest'))

    def test_price_by_night(self):
        """ """
        self.assertTrue(hasattr(self.value, 'price_by_night'))

    def test_latitude(self):
        """ """
        self.assertTrue(hasattr(self.value, 'latitude'))

    def test_longitude(self):
        """ """
        self.assertTrue(hasattr(self.value, 'longitude'))

    # def test_amenity_ids(self):
    #     """ """
    #     self.assertTrue(hasattr(self.value), '')
