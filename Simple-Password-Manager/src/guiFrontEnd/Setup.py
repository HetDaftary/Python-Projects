import sys
from src.working.setup import main as setup
from src.working.setup import fileName
from PyQt5 import QtWidgets as qtw
from darkdetect import isDark
from qt_material import apply_stylesheet
from os.path import exists

size = 960, 540
darkTheme, lightTheme = 'dark_blue.xml', 'light_blue.xml'
styleNames = ["OS preferred", "light Theme", "dark theme"]

def updateQLabel(label, text):
    label.setText(text)
    label.adjustSize()

class MainWindow(qtw.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initMenuBar()
        
    def initUI(self):
        self.resize(*size)

        self.mainWin = qtw.QWidget()
        layout = qtw.QVBoxLayout()
        self.mainWin.setLayout(layout)

        hBoxWidget = qtw.QWidget()
        hlayout = qtw.QHBoxLayout()
        hBoxWidget.setLayout(hlayout)

        passwordLabel = qtw.QLabel("Enter primary password: ")
        hlayout.addWidget(passwordLabel)
        passwordLineEdit = qtw.QLineEdit()
        hlayout.addWidget(passwordLineEdit)
        passwordLineEdit.setEchoMode(qtw.QLineEdit.Password)

        layout.addWidget(hBoxWidget)

        self.statusLine = qtw.QLabel("")
        layout.addWidget(self.statusLine)

        self.makeDatabaseButtuon = qtw.QPushButton("Make Database")
        layout.addWidget(self.makeDatabaseButtuon)

        self.setCentralWidget(self.mainWin)
        self.show()

    def initMenuBar(self):
        self.menuBar = qtw.QMenuBar()
        self.themeMenu = qtw.QMenu("Theme Menu")

        self.osPreferredTheme = qtw.QAction("OS preferred Theme")
        self.themeMenu.addAction(self.osPreferredTheme)
        self.lightTheme = qtw.QAction("Light Theme")
        self.themeMenu.addAction(self.lightTheme)
        self.darkTheme = qtw.QAction("Dark Theme")
        self.themeMenu.addAction(self.darkTheme)

        self.menuBar.addMenu(self.themeMenu)
        self.setMenuBar(self.menuBar)

class GUI(qtw.QApplication):
    def __init__(self) -> None:
        super().__init__(["Simple password manager setup"])
        self.mainWindow = MainWindow()
        self.initWorking()
        self.initMenuActions()
        sys.exit(self.exec_())
    
    def initMenuActions(self):
        self.mainWindow.osPreferredTheme.triggered.connect(lambda: self.changeStyle(self.mainWindow.osPreferredTheme))
        self.mainWindow.lightTheme.triggered.connect(lambda: self.changeStyle(self.mainWindow.lightTheme))
        self.mainWindow.darkTheme.triggered.connect(lambda: self.changeStyle(self.mainWindow.darkTheme))


    def initWorking(self):
        self.currentStyle = 0
        self.changeStyle(self.mainWindow.osPreferredTheme)
        self.mainWindow.makeDatabaseButtuon.clicked.connect(self.doSetup)

    def doSetup(self):
        if exists(fileName):
            setup(
                self.mainWindow.passwordLineEdit.text()
            )
            updateQLabel(self.mainWindow.statusLine, "Updated")
        else:
            updateQLabel(self.mainWindow.statusLine, "Database already exists")

    def changeStyle(self, menuAction):
        global darkTheme, lightTheme
        global styleNames

        if self.currentStyle == 0:
            self.mainWindow.osPreferredTheme.setText(styleNames[0])
        elif self.currentStyle == 1:
            self.mainWindow.lightTheme.setText(styleNames[1])
        else:
            self.mainWindow.darkTheme.setText(styleNames[2])

        if menuAction == self.mainWindow.lightTheme:  
            apply_stylesheet(self, lightTheme)
            self.currentStyle = 1
        elif menuAction == self.mainWindow.darkTheme:
            apply_stylesheet(self, darkTheme)
            self.currentStyle = 2
        else:
            self.currentStyle = 0
            if isDark():
                apply_stylesheet(self, darkTheme)
            else:
                apply_stylesheet(self, lightTheme)

        menuAction.setText(f"✔️{menuAction.text()}")

def main():
    gui = GUI()