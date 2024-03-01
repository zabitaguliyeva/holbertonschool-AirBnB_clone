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

