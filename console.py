#!/usr/bin/python3
""" Console for the AirBnB_clone project """
import cmd
from models import *


class airbnb(cmd.Cmd):
    """airbnb class

    Console class for airbnb

    """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ EOF command to exit the command interpreter """
        quit()

    # def do_help(self, arg):
    #     """ Provides description of a given command """

    def do_quit(self, arg):
        """ Exits the console after "quit" is entered """
        quit()

if __name__ == "__main__":
    airbnb().cmdloop()