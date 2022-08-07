#!/usr/bin/python3
"""
Entry of commands
"""

import cmd
from models.base_model import BaseModel
from models import class_name
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n """
        return True

    def do_EOF(self, arg):
        """ EOF is added """
        print()
        return True

    def emptyline(self):
        """empty line if no command is given"""
        pass

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg in class_name:
            classes = class_name[arg]()
            print(classes.id)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of the instance class and id"""
        argv = arg.split()
        try:
            key = argv[0] + "." + argv[1]
        except Exception:
            pass

        if len(arg) == 0:
            print("** class name missing **")
        else:
            if argv[0] in class_name:
                if len(argv) < 2:
                    print("** instance id missing **")
                elif key in storage.all().keys():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        argv = arg.split()
        try:
            key = argv[0] + "." + argv[1]
        except Exception:
            pass

        if len(arg) == 0:
            print("** class name missing **")
        else:
            if argv[0] in class_name:
                if len(argv) < 2:
                    print("** instance id missing **")
                elif key in storage.all().keys():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
            elif argv[0] not in class_name:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        argv = arg.split()
        if len(argv) > 0 and argv[0] not in class_name:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in storage.all().values():
                if len(argv) > 0 and argv[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(argv) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        argv = arg.split()
        try:
            key = argv[0] + "." + argv[1]
        except Exception:
            pass

        if len(arg) == 0:
            print("** class name missing **")
        else:
            if argv[0] in class_name:
                if len(argv) < 2:
                    print("** instance id missing **")
                elif len(argv) < 3:
                    print("** attribute name missing **")
                elif len(argv) < 4:
                    print("** value missing **")
                elif key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    for key, value in storage.all().items():
                        if argv[1] == value.id:
                            setattr(value, argv[2], argv[3].strip('"'))
                            storage.save()
            else:
                print("** class doesn't exist **")

    def do_count(self, line):
        """Display count of instances specified"""
        if line in class_name:
            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """Accepts class name followed by arguement"""
        args = line.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(line))
            return
        try:
            args = args[1].split('(')
            command = args[0]
            if command == 'all':
                HBNBCommand.do_all(self, class_arg)
            elif command == 'count':
                HBNBCommand.do_count(self, class_arg)
            elif command == 'show':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_show(self, arg)
            elif command == 'destroy':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_destroy(self, arg)
            elif command == 'update':
                args = args[1].split(',')
                id_arg = args[0].strip("'")
                id_arg = id_arg.strip('"')
                name_arg = args[1].strip(',')
                val_arg = args[2]
                name_arg = name_arg.strip(' ')
                name_arg = name_arg.strip("'")
                name_arg = name_arg.strip('"')
                val_arg = val_arg.strip(' ')
                val_arg = val_arg.strip(')')
                arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.do_update(self, arg)
            else:
                print("*** Unknown syntax: {}".format(line))
        except IndexError:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
