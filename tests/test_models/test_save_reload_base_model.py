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

class TestUserSaveReload(unittest.TestCase):
    """Unittests for testing save and reload methods of the User class."""

    def setUp(self):
        """Set up test environment."""
        try:
            storage.reload()
        except:
            pass

    def tearDown(self):
        """Tear down test environment."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_reload_objects(self):
        """Test that objects are reloaded from the file storage."""
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 0)

        print("-- Create a new User --")
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()
        self.assertIn(f"User.{my_user.id}", storage.all())
        print(my_user)

        print("-- Create a new User 2 --")
        my_user2 = User()
        my_user2.first_name = "John"
        my_user2.email = "airbnb2@mail.com"
        my_user2.password = "root"
        my_user2.save()
        self.assertIn(f"User.{my_user2.id}", storage.all())
        print(my_user2)

if __name__ == "__main__":
    unittest.main()