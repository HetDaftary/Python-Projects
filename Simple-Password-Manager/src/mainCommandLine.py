from src.frontend.Setup import main as setupMain
from src.working import fileName
from src.frontend.working import main as workingMain
from os.path import exists

if __name__ == "__main__":
    if exists(fileName):
        workingMain()
    else:
        setupMain()