import shutil
import sys
import time

def set_string():
    string = "aaaa"
    return string


def show():
    # string = "aaaaaaaaaaaa"
    string = set_string()
    terminal_size = shutil.get_terminal_size()
    for i in range(terminal_size.columns):

        sys.stdout.write("\r{}".format(" " * i + string + " " * (terminal_size.columns - i)))
        sys.stdout.flush()
        time.sleep(0.1)