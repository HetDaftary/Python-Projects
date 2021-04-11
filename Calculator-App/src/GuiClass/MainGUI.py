from PyQt5.QtWidgets import *
from sys import exit
from qt_material import apply_stylesheet
from darkdetect import isDark

darkTheme, lightTheme = 'dark_blue.xml', 'light_blue.xml'

class GUI:
    buttonText = [['9', '8', '7', '+'], ['6', '5', '4', '-'], ['1', '2', '3', 'x'], ['0', 'enter', 'clear', '/']]
    size = 600, 400

    def __init__(self):
        self.app = QApplication(["Calculator"])
        self.mainWindow = QMainWindow()
        self.mainWindow.resize(*(GUI.size))
        
        self.mainWin = QWidget()
        self.mainWindow.setCentralWidget(self.mainWindow)

        self.initUI()
        self.initMenubar()

        self.mainWindow.show()
        exit(self.app.exec_())

    def initUI(self):
        vLayout = QVBoxLayout()
        self.mainWin.setLayout(vLayout)

        self.mainEntry = QLineEdit()
        self.mainEntry.resize(200, 400)
        vLayout.addWidget(self.mainEntry)

        # Time for buttons.
        self.buttonsWid = QWidget()
        gridLayout = QGridLayout()
        self.buttonsWid.setLayout(gridLayout)

        self.buttons = []

        for i in range(len(GUI.buttonText)):
            self.buttons.append([])
            for j in range(len(GUI.buttonText)):
                self.buttons[i].append(QPushButton(GUI.buttonText[i][j]))
                self.buttons[i][j].clicked.connect(lambda _, i = i, j = j : self.onPress(i, j))
                gridLayout.addWidget(self.buttons[i][j], i, j)

        vLayout.addWidget(self.buttonsWid)

    def initMenubar(self):
        global darkTheme, lightTheme

        self.menubar = QMenuBar()

        self.themeMenu = QMenu("Theme Menu")

        self.lightThemeAction = QAction("Light Theme")
        self.lightThemeAction.triggered.connect(lambda : self.setTheme(lightTheme))
        self.themeMenu.addAction(self.lightThemeAction)

        self.darkThemeAction = QAction("Dark Theme")
        self.darkThemeAction.triggered.connect(lambda : self.setTheme(darkTheme))
        self.themeMenu.addAction(self.darkThemeAction)

        self.menubar.addMenu(self.themeMenu)

        self.mainWindow.setMenuBar(self.menubar)

        if isDark():
            self.setTheme(darkTheme)
        else:
            self.setTheme(lightTheme)

    def onPress(self, i, j):
        if i == 3 and j == 1:
            self.mainEntry.setText(str(eval(self.mainEntry.text())))
        elif i == 3 and j == 2:
            self.mainEntry.setText("")
        else:
            self.mainEntry.setText(self.mainEntry.text() + GUI.buttonText[i][j])

    def setTheme(self, theme):
        apply_stylesheet(self.app, theme)