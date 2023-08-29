#!/usr/bin/python3
""" Console Module """
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    # ... (rest of your code)

    def do_create(self, args):
        """ Create an object of any class"""
        arg2 = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        elif arg2[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[arg2[0]]()
        arg2 = arg2[1:]
        for arg in arg2:
            try:
                new_list = list(arg.split('='))
            except Exception:
                continue
            key = new_list[0]
            value = new_list[1]
            try:
                test = int(value)
                if len(str(test)) == len(value):
                    value = test
            except Exception:
                try:
                    value = float(value)
                except Exception:
                    value = value.replace('_', ' ')
            if hasattr(new_instance, key):
                setattr(new_instance, key, value)
        print(new_instance.id)
        new_instance.save()

    # ... (rest of your code)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
