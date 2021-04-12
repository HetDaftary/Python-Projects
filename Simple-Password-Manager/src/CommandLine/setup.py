from src.Working.setup import setup
from src.Working.setup import fileName
from os.path import exists
from getpass import getpass 

def main():
    if exists(fileName):
        raise "File Exists"
    else:
        setup(getpass(prompt="Enter primary password: "))