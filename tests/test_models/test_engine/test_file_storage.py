import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class TestFileStorage(unittest.TestCase):
    def test_save(self):
        instance = BaseModel()
        instance.save()
        with open("file.json", "r") as f:
           data = json.load(f)
           self.assertIn("BaseModel." + instance.id, data)

    def test_all(self):
        base_instance = BaseModel()
        fs_instance = FileStorage()
        self.assertIn(base_instance, fs_instance.all().values())