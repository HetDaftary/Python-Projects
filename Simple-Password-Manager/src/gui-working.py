from Working import Working
from PyQt5.QtWidgets import *
from sys import argv, exit
import qdarkstyle

class GUI:
    def __init__(self):
        self.app = QApplication(["Simple-Password-Manager-Working"])
        self.app.setStyleSheet(qdarkstyle.load_stylesheet())
        self.mainWin = QWidget()
        self.mainWinLayout = QBoxLayout()
        self.mainWin.setLayout(mainWinLayout)

        self.initUI()

        self.mainWin.show()
        exit(self.app.exec_())

    def initUI(self):
        self.loginPage = QWidget()
        self.workingPage = QWidget()
        self.changePasswordPage = QWidget()

        self.initLoginPage()
        self.initWorkingPage()
        self.initChangePasswordPage()

    def initLoginPage(self):
        pass

    def initWorkingPage(self):
        pass

    def initChangePasswordPage(self):
        pass 

if __name__ == "__main__":
    gui = GUI()