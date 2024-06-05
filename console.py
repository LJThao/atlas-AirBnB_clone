#!/usr/bin/python3
"""Command Interpreter"""


import cmd
from models import *


class HBNBCommand(cmd.Cmd):
    """Class defining the Command interpreter for HBNB"""
    prompt = '(hbnb) '

    def do_quit(self, command_arg):
        """Function to quit the command and exit"""
        return (True)

    def do_EOF(self, command_arg):
        """Function to use EOF(end of file)
        command to exit -- Ctrl+D"""
        print()
        return (True)

    def emptyline(self):
        """Function that does nothing on an empty input
        line + ENTER"""
        pass

    def do_create(self, command_arg):
        """Creates a new instance of BaseModel"""
        if command_arg == "" or command_arg is None:
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
        """Prints the string rep of an instance based on
        the class name and id"""
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
