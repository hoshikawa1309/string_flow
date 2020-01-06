import shutil
import sys
import time
import os


def set_string():
    with open("venv/template/logo.txt" , "r") as open_file:
        logo_list = open_file.read().split("\n")
    return logo_list


def show():
    logo_list = set_string()
    terminal_size = shutil.get_terminal_size()
    for i in range(terminal_size.columns):
        string = ""
        for row in logo_list:
            string += " " * i + row + "\n"
        # string = " " * i + "i"
        sys.stdout.write("{}\r\033[50A".format(string))
        sys.stdout.flush()

        # time.sleep(0.1)