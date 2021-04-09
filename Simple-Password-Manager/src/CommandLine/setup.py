from src.Working.setup import setup
from src.Working.setup import fileName
from os.path import exists

def main():
    if exists(fileName):
        raise "File Exists"
    else:
        setup(input("Enter primary password: "))