from ..Functions.Functions import crop
# The crop functionality.

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from sys import argv, exit

class CropGUI:
    def __init__(self, img):
        self.initUI(img)

    def initUI(self):
        self.app = QApplication(argv)
        self.win = QMainWindow() 
        self.win.setWindowTitle("Crop-GUI")
        self.win.setGeometry(200, 200, 700, 700)
        
        

        self.win.show()
        exit(self.app.exec_())