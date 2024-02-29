#!/usr/bin/python3

"""basic console"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = ["BaseModel", "xcv"]

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        pass

    do_EOF = do_quit

    def do_create(self, arg):
        """create instance"""

        args = arg.split()

        if not args[0]:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj = eval(args[0])()
            obj.save()
            id = obj.id
            print(id)

    def do_show(self, arg):
        comand = arg.split()
        if len(comand) == 0:
            print("** class name missing **")
        elif comand[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(comand) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            obj_key = arg[0] + "." + arg[1]
            if obj_key in obj:
                print(obj[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        comand = arg.split()
        if len(comand) == 0:
            print("** class name missing **")
        elif comand[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(comand) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            obj_key = comand[0] + "." + comand[1]
            if obj_key in obj:
                del(obj[obj_key])
                storage.save()
            else:
                print("** no instance found **")







if __name__ == "__main__":
    HBNBCommand().cmdloop()
