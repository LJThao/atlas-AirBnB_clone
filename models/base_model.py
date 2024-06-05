# models/base_model.py

import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "created_at" in kwargs:
                self.created_at = datetime.fromisoformat(kwargs["created_at"])
            if "updated_at" in kwargs:
                self.updated_at = datetime.fromisoformat(kwargs["updated_at"])

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Returns a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
