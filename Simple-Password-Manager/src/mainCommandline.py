from src.CommandLine import setup
from src.CommandLine import working
from os.path import exists
from src.CommandLine.setup import fileName

if __name__ == "__main__":
    if exists(fileName):
        working.main()
    else:
        setup.main()