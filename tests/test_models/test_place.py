#!/usr/bin/python3
""" file that tests the place class """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ tests the place class """

    def __init__(self, *args, **kwargs):
        """ initialization """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ tests city id """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ tests user id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ tests name id """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ tests description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test number of rooms """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ tests number of bathrooms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ tests max_guest """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ tests price_by_night """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ tests latitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ tests longitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ tests amenity_ids """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
