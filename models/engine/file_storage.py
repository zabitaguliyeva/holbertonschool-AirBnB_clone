#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
            for k, value in data.values():
                class_name = k.split(".")[0]
                self.__objects[k] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
            