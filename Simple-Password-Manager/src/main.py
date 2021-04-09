from .GUI import setup
from .GUI import working
from os.path import exists
from sys import platform
from src.GUI.setup import fileName

if __name__ == '__main__':
    if exists(fileName):
        gui = working.GUI()
    else:
        gui = setup.GUI()