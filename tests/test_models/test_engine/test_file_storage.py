import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def test_save(self):
        instance = BaseModel()
        instance.save()
        self.assertIn("BaseModel." + instance.id, storage.all())