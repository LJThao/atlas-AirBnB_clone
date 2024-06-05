# models/engine/file_storage.py

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name = value['__class__']
                cls = globals()[cls_name]
                self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        return {"BaseModel": BaseModel, "User": User}

