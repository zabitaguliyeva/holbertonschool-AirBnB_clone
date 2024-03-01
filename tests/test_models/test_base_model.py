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

    def test_todict(self):
        instance = BaseModel()
        new_dict = instance.to_dict()
        self.assertTrue(new_dict)

    def test_str(self):
        instance = BaseModel()
        res = instance.__str__()
        self.assertEqual(res, "[{}] ({}) {}".format(instance.__class__.__name__, instance.id, vars(instance)))
        