#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects

    def test_file_path(self):
        self.assertEqual(type(self.file_path), str)

    def test_objects(self):
        self.assertEqual(type(self.objects), dict)

    def test_all(self):
        objs = storage.all()
        self.assertEqual(type(objs), dict)

    def test_new(self):
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, self.objects)

    def test_save(self):
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, self.objects)
        storage.save()
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
            self.assertTrue(lines)

    def test_reload(self):
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        storage.reload()
        self.assertIn(key, self.objects)

    def test_base_model_init(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_base_model_save(self):
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(prev_updated_at, obj.updated_at)


if __name__ == '__main__':
    unittest.main()