from setup import setup
from PyQt5.QtWidgets import *
from sys import exit
import qdarkstyle

class GUI:
    def __init__(self):
        self.app = QApplication(["Simple-Password-Manager-Setup"])
        self.app.setStyleSheet(qdarkstyle.load_stylesheet())
        self.win = QWidget()

        self.initUI()

        self.win.show()
        exit(self.app.exec_())

    def initUI(self):
        layout = QVBoxLayout()
        self.win.setLayout(layout)
        
        hLayout = QHBoxLayout()
        wid = QWidget()
        wid.setLayout(hLayout)

        self.lab = QLabel(text = "Enter Password:")
        self.lab.adjustSize()
        self.input = QLineEdit()
        self.input.setEchoMode(QLineEdit.Password)
        self.b = QPushButton(text = "Make-Database")
        self.b.clicked.connect(self.onPress)

        hLayout.addWidget(self.lab)
        hLayout.addWidget(self.input)

        layout.addWidget(wid)
        layout.addWidget(self.b)

    def onPress(self):
        setup(self.input.text())

if __name__ == "__main__":
    gui = GUI()