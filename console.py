#!/usr/bin/python3

"""basic console"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = ["BaseModel", "sss"]

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        pass

    do_EOF = do_quit

    def do_create(self, arg):
        """create instance"""

        if not arg:
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj = eval(arg)()
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
            obj_key = comand[0] + "." + comand[1]
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
                del (obj[obj_key])
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        comand = arg.split()
        obj = storage.all()
        if len(comand) == 0:
            for v in obj.values():
                print(v)
        elif comand[0] not in self.__classes:
            print("**class doesn't exist**")
        else:
            class_name = comand[0]
            result_list = [str(v) for k, v in obj.items()
                           if k.startswith(class_name + ".")]
            print(result_list)

    def do_update(self, arg):
        comand = arg.split()
        if len(comand) == 4:
            data = storage.all()
            key = "{}.{}".format(comand[0], comand[1])
            if (key not in storage.all()):
                print("** no instance found **")
            else:
                for k, v in data.items():
                    if comand[1] == k.split('.')[1]:
                        setattr(v, comand[2], comand[3].split("\"")[1])
                        storage.save()

        if len(comand) == 3:
            print("** value missing **")

        if len(comand) == 2:
            key = "{}.{}".format(comand[0], comand[1])
            if (key not in storage.all()):
                print("** no instance found **")
            else:
                print("** attribute name missing **")

        if len(comand) == 1:
            print("** instance id missing **")

        if len(comand) == 0:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
