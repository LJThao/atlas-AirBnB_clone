#!/usr/bin/python3
"""Command Interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class defining the Command interpreter for HBNB"""
    prompt = '(hbnb) '

    def do_quit(self, command_arg):
        """Function to quit the command and exit"""
        return True

    def do_EOF(self, command_arg):
        """Function to use EOF(end of file) command to exit -- Ctrl+D"""
        print()
        return True

    def emptyline(self):
        """Function that does nothing on an empty input line + ENTER"""
        pass

    def do_create(self, command_arg):
        """Creates a new instance of BaseModel"""
        if not command_arg:
            print("** class name missing **")
            return
        elif command_arg not in storage.classes():
            print("** class doesn't exist **")
            return
        else:
            cls = storage.classes()[command_arg]
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, command_arg):
        """Prints the string rep of an instance based on the class name and id"""
        if not command_arg:
            print("** class name missing **")
            return

        parts = command_arg.split(' ')
        if parts[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(parts) < 2:
            print("** instance id missing **")
            return

        insta_key = "{}.{}".format(parts[0], parts[1])
        instance = storage.all().get(insta_key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, command_arg):
        """Delete an instance based on the class name and id"""
        if not command_arg:
            print("** class name missing **")
            return
        parts = command_arg.split(' ')
        if parts[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        key = f"{parts[0]}.{parts[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, command_arg):
        """Prints all string representation of all instances"""
        if command_arg:
            if command_arg not in storage.classes():
                print("** class doesn't exist **")
                return
            objs = [str(obj) for key, obj in storage.all().items()
                    if key.startswith(command_arg)]
        else:
            objs = [str(obj) for obj in storage.all().values()]
        print(objs)

    def do_update(self, command_arg):
        """Updates an instance based on the class name and id"""
        if not command_arg:
            print("** class name missing **")
            return
        parts = command_arg.split(' ')
        if parts[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        if len(parts) < 3:
            print("** attribute name missing **")
            return
        if len(parts) < 4:
            print("** value missing **")
            return
        key = f"{parts[0]}.{parts[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        setattr(obj, parts[2], parts[3])
        obj.save()

    def default(self, line):
        """Handle unrecognized commands"""
        parts = line.split('.')
        if len(parts) == 2 and parts[1] == "all()":
            class_name = parts[0]
            self.do_all(class_name)
        else:
            print(f"*** Unknown syntax: {line}")

    def do_count(self, command_arg):
        """Count the number of instances of a class"""
        if not command_arg:
            print("** class name missing **")
            return
        if command_arg not in storage.classes():
            print("** class doesn't exist **")
            return
        count = 0
        for key in storage.all().keys():
            if key.startswith(command_arg):
                count += 1
        print(count)

    def do_show(self, command_arg):
        """Retrieve an instance based on its ID"""
        if not command_arg:
            print("** class name missing **")
            return
        parts = command_arg.split(' ')
        if parts[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(parts[0], parts[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, command_arg):
        """Destroy an instance based on its ID"""
        if not command_arg:
            print("** class name missing **")
            return
        parts = command_arg.split(' ')
        if parts[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(parts[0], parts[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_update(self, command_arg):
        """Update an instance based on its ID"""
        if not command_arg:
            print("** class name missing **")
            return
        parts = command_arg.split(' ')
        if parts[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(parts[0], parts[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(parts) < 3:
            print("** attribute name missing **")
            return
        if len(parts) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, parts[2], parts[3])
        storage.save()

    def do_all(self, command_arg):
        """Retrieve all instances of a class"""
        if not command_arg:
            print("** class name missing **")
            return
        if command_arg not in storage.classes():
            print("** class doesn't exist **")
            return
        objs = storage.all().values()
        objs_filtered = [str(obj) for obj in objs if obj.__class__.__name__ == command_arg]
        print(objs_filtered)
    

    def do_update(self, command_arg):
        """Update an instance based on its ID with a dictionary"""
        if not command_arg:
            print("** class name missing **")
            return
        parts = command_arg.split(' ')
        if parts[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(parts[0], parts[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(parts) < 3:
            print("** dictionary missing **")
            return
        obj = storage.all()[key]
        try:
            dictionary = eval(parts[2])
        except Exception as e:
            print("** invalid dictionary **")
            return
        for k, v in dictionary.items():
            setattr(obj, k, v)
        storage.save()

    def do_all(self, command_arg):
        """Retrieve all instances"""
        if command_arg:
            if command_arg not in storage.classes():
                print("** class doesn't exist **")
                return
            objs = [str(obj) for obj in storage.all().values()
                    if type(obj).__name__ == command_arg]
        else:
            objs = [str(obj) for obj in storage.all().values()]
        print(objs)

    def do_show(self, command_arg):
        """Show instance by ID"""
        if not command_arg:
            print("** class name missing **")
        return
    
    parts = command_arg.split(' ')
    if parts[0] not in storage.classes():
        print("** class doesn't exist **")
        return

    if len(parts) < 2:
        print("** instance id missing **")
        return

    insta_key = "{}.{}".format(parts[0], parts[1])
    instance = storage.all().get(insta_key)
    if instance:
        print(instance)
    else:
        print("** no instance found **")

def do_destroy(self, command_arg):
    """Destroy instance by ID"""
    if not command_arg:
        print("** class name missing **")
        return

    parts = command_arg.split(' ')
    if parts[0] not in storage.classes():
        print("** class doesn't exist **")
        return

    if len(parts) < 2:
        print("** instance id missing **")
        return

    insta_key = "{}.{}".format(parts[0], parts[1])
    if insta_key not in storage.all():
        print("** no instance found **")
        return

    del storage.all()[insta_key]
    storage.save()

def do_update_from_dict(self, command_arg):
    """Update instance from dictionary by ID"""
    if not command_arg:
        print("** class name missing **")
        return

    parts = command_arg.split(' ')
    if parts[0] not in storage.classes():
        print("** class doesn't exist **")
        return

    if len(parts) < 2:
        print("** instance id missing **")
        return

    if len(parts) < 3:
        print("** dictionary missing **")
        return

    insta_key = "{}.{}".format(parts[0], parts[1])
    obj = storage.all().get(insta_key)
    if not obj:
        print("** no instance found **")
        return

    try:
        data_dict = eval(parts[2])
    except Exception as e:
        print("** invalid dictionary **")
        return

    for key, value in data_dict.items():
        setattr(obj, key, value)
    obj.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()

    
