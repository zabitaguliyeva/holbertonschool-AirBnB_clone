import unittest
from models.base_model import BaseModel
from models import storage

class TestBaseModel(unittest.TestCase):
    def test_save(self):
       instance = BaseModel()
       instance.save()
       self.assertIn("BaseModel." + instance.id, storage.all())
