import commandLine
import commandlineSetup
from os.path import exists

fileName = "../data/2.db"

if __name__ == "__main__":
    if exists(fileName):
        commandLine.main()
    else:
        commandlineSetup.main()