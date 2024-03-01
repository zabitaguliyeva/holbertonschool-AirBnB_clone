#!/usr/bin/python3
"""Unit tests for the City class"""

import os
import unittest

from models import storage
from models.city import City

class TestAmenity(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

        storage.__objects = {}

    def test_check_type(self):
        self.assertIsInstance(City.name, str)
        self.assertIsInstance(City.state_id, str)

    def test_name(self):
        city_model = City()
        city_model.name = "Baku"
        self.assertEqual(city_model.name, "Baku")

    def test_state_id(self):
        city_model = City()
        city_model.state_id = "31"
        self.assertEqual(city_model.state_id, "31")