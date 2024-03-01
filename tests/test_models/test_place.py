#!/usr/bin/python3
"""Place model test"""

import unittest
from models.place import Place

class TestPlaceModel(unittest.TestCase):
    def setUp(self):
        self.place = Place(
            city_id="1",
            user_id="1",
            name="Good Hotel",
            description="Very good place",
            number_rooms=3,
            number_bathrooms=2,
            max_guest=6,
            price_by_night=99,
            latitude=74.16,
            longitude=68.92,
            amenity_ids=[]
        )

    def test_types(self):
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_attributes(self):
        self.assertEqual(self.place.city_id, "1")
        self.assertEqual(self.place.user_id, "1")
        self.assertEqual(self.place.name, "Good Hotel")
        self.assertEqual(self.place.description, "Very good place")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 6)
        self.assertEqual(self.place.price_by_night, 99)
        self.assertEqual(self.place.latitude, 74.16)
        self.assertEqual(self.place.longitude, 68.92)
        self.assertEqual(self.place.amenity_ids, [])

if __name__ == '__main__':
    unittest.main()
