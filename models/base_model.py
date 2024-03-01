#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, vars(self))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        res = self.__dict__.copy()
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()
        res["__class__"] = self.__class__.__name__
        return res
