from PyQt5.QtWidgets import *
from sys import argv, exit
import sys

sys.path.insert(1, "../../src/")


from ..Working.setup import setup, fileName
from qt_material import apply_stylesheet
from os.path import exists

# Global constants.
size = 960, 540
darkTheme, lightTheme = 'dark_blue.xml', 'light_blue.xml'

class GUI:
    def __init__(self):
        self.app = QApplication(argv)
        self.mainWindow = QMainWindow()
        self.mainWindow.resize(*size)
        self.mainWin = QWidget()
        self.mainWindow.setCentralWidget(self.mainWin)

        self.initUI()
        self.initWorking()
        self.initMenuBar()

        self.mainWindow.show()
        exit(self.app.exec_())

    def initUI(self):
        vLayout = QVBoxLayout()
        self.mainWin.setLayout(vLayout)
        hLayout = QHBoxLayout()
        passwordEntry = QWidget()
        passwordEntry.setLayout(hLayout)

        entryLabel = QLabel("Enter Password:")
        hLayout.addWidget(entryLabel)
        self.passwordEntry = QLineEdit()
        self.passwordEntry.setEchoMode(QLineEdit.Password)
        hLayout.addWidget(self.passwordEntry)

        vLayout.addWidget(passwordEntry)

        self.errorsLabel = QLabel()
        vLayout.addWidget(self.errorsLabel)

        button = QPushButton("Setup database")
        button.clicked.connect(self.buttonWork)
        vLayout.addWidget(button)

    def initWorking(self):
        global darkTheme
        self.setTheme(darkTheme)

    def initMenuBar(self):
        global lightTheme, darkTheme
        self.menuBar = QMenuBar(self.mainWindow)
        self.mainWindow.setMenuBar(self.menuBar)

        self.themeMenu = QMenu("Theme Menu")
        self.menuBar.addMenu(self.themeMenu)

        self.lightThemeItem = QAction("Light Theme")
        self.lightThemeItem.triggered.connect(lambda : self.setTheme(lightTheme))
        self.themeMenu.addAction(self.lightThemeItem)

        self.darkThemeItem = QAction("Dark Theme")
        self.darkThemeItem.triggered.connect(lambda: self.setTheme(darkTheme))
        self.themeMenu.addAction(self.darkThemeItem)

        self.menuBar.addMenu(self.themeMenu)

    def setTheme(self, themeToSet):
        apply_stylesheet(self.app, themeToSet)

    def buttonWork(self):
        if exists(fileName):
            self.errorsLabel.setText("Database already present.")
            self.errorsLabel.adjustSize()
        else:
            setup(self.passwordEntry.text())
            self.errorsLabel.setText("Done. Setup Complete")
            self.errorsLabel.adjustSize()