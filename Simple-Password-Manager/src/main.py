import guiSetup
import guiWorking
from os.path import exists

fileName = "../data/2.db"

if __name__ == "__main__":
    gui = None 
    if exists(fileName):
        gui = guiWorking.GUI()
    else:
        gui = guiSetup.GUI()