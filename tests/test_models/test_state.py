#!/usr/bin/python3
"""Unit tests for State class"""


import unittest
from models.state import State

class TestStateModel(unittest.TestCase):
    def setUp(self):
        self.state = State()
        self.state.name = "State"

    def test_type(self):
        self.assertIsInstance(State.name, str)

    def test_name(self):
        self.assertEqual(self.state.name, "State")