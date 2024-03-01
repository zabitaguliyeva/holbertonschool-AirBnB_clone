#!/usr/bin/python3
"""Unit tests for Review class"""


import unittest
from models.review import Review


class TestReviewModel(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.review.place_id = "31a05726-d68b-40d7-b057-5014d0f5082e"
        self.review.user_id = "140d7-b057-5014d0f5082e"
        self.review.text = "review"

    def test_type(self):
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

    def test_place_id(self):
        self.assertEqual(self.review.place_id, "31a05726-d68b-40d7-b057-5014d0f5082e")

    def test_user_id(self):
        self.assertEqual(self.review.user_id, "140d7-b057-5014d0f5082e")

    def test_text(self):
        self.assertEqual(self.review.text, "review")