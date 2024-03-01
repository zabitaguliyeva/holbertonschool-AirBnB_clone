import unittest
from models import storage
from models.base_model import BaseModel
import json


class TestFileStorage(unittest.TestCase):
    def test_save(self):
        instance = BaseModel()
        instance.save()
        with open("file.json", "r") as f:
           data = json.load(f)
           self.assertIn("BaseModel." + instance.id, data)