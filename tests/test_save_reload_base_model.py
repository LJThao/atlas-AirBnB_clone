#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User

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

class TestSaveReloadBaseModel(unittest.TestCase):
    """Unittests for testing save and reload methods of the BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Tear down test environment."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_save_reload(self):
        """Test save and reload methods."""
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 0)

        # Create a new object
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        all_objs = storage.all()
        self.assertEqual(len(all_objs), 1)

        # Create a new object after saving
        my_model2 = BaseModel()
        my_model2.name = "My_Second_Model"
        my_model2.my_number = 42
        my_model2.save()

        all_objs = storage.all()
        self.assertEqual(len(all_objs), 2)

        # Check if objects are reloaded properly
        storage.reload()
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 2)
        self.assertIn(my_model.id, all_objs)
        self.assertIn(my_model2.id, all_objs)
        self.assertEqual(all_objs[my_model.id].name, "My_First_Model")
        self.assertEqual(all_objs[my_model.my_number], 89)
        self.assertEqual(all_objs[my_model2.id].name, "My_Second_Model")
        self.assertEqual(all_objs[my_model2.my_number], 42)

if __name__ == "__main__":
    unittest.main()