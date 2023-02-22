#!/usr/bin/python3
import cmd
import sys
import os
from models import storage
from models.base_model import BaseModel
from models.users import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        ''' Exit the program'''
        return True

    def do_EOF(self, arg):
        ''' Exit the program using EOF'''
        return True

    def empty_line(self, arg):
        ''' Do nothing when empty line entered'''
        pass

    def do_create(self, arg):
        if len(arg) == 0:
            print('** class name missing **')
            return False
        if arg not in ls:
            print("** class doesn't exist **")
            return False
        new = eval(arg)()
        storage.save()
        print(new.id)

    def do_show(self, arg):
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in ls:
            print("** class doesn't exist **")
            return False
        if len(arg) != 2:
            print("** instance id missing ** ")
        check = arg[0] + '.' + arg[1]
        if check in storage.all().keys():
            print(storage.all()[check])
        else:
            print('** no instance found **')

    def do_destroy(self, arg):
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in ls:
            print("** class doesn't exist **")
            return False
        if len(arg) != 2:
            print("** instance id missing ** ")
            return False
        check = arg[0] + '.' + arg[1]
        if check in storage.all().keys():
            del storage.all()[check]
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, arg):
        if len(arg) != 0:
            if arg not in ls:
                print("** class doesn't exist **")
                return False
            for key, value in storage.all().items():
                if value.__class__.__name__ == arg:
                    print(value)
        else:
            for key, value in storage.all().items():
                print(value)

    def do_update(self, arg):
        arg = arg.split()
        flag = 0
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in ls:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        for key, value in storage.all().items():
            if value.id == (arg[1]):
                flag += 1
        if flag == 0:
            print("** no instance found **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            print("** value missing **")
            return False
        val = arg[3].split('"')
        setattr(value, arg[2], val[1])
        storage.save()


if __name__ == '__main__':
    ls = ['BaseModel', 'User', 'City', 'State', 'Review', 'Amenity']
    HBNBCommand().cmdloop()