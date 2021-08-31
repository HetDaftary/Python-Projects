from src.guiFrontEnd.Setup import main as setupMain
from src.guiFrontEnd.working import main as workingMain
from src.guiFrontEnd.working import fileName
from os.path import exists

if exists(fileName):
    workingMain()
else:
    setupMain()