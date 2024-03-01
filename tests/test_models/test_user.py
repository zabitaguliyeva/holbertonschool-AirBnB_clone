#!/usr/bin/python3

import os
import unittest
from models import storage
from models.user import User

class TestUser(unittest.Testcase):
    """Unit tests for the User class"""

    def setUp(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        storage.__objects = {}

    def test_user_email(self):
        user_model = User()
        user_model.email = "7644@holbertonstudents.com"
        self.assertEqual(user_model.email, "7644@holbertonstudents.com")

    def test_type(self):
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_email(self):
        user = User()
        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")

    def test_password(self):
        user = User()
        user.password = "password123"
        self.assertEqual(user.password, "password123")

    def test_first_name(self):
        user = User()
        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_last_name(self):
        user = User()
        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")

