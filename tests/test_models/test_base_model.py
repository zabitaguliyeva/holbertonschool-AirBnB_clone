import unittest
from models.base_model import BaseModel
from models import storage
import json

class TestBaseModel(unittest.TestCase):
    def test_save(self):
       instance = BaseModel()
       instance.save()
       with open("file.json", "r") as f:
           data = json.load(f)
           self.assertIn("BaseModel." + instance.id, data)
