import unittest
from models.base_model import BaseModel
from models import storage
import json
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_save(self):
       instance = BaseModel()
       instance.save()
       with open("file.json", "r") as f:
           data = json.load(f)
           self.assertIn("BaseModel." + instance.id, data)

    def test_todict(self):
        instance = BaseModel()
        new_dict = instance.to_dict()
        self.assertTrue(new_dict)
        
        