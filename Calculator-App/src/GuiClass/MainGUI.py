from PyQt5.QtWidgets import *
from sys import exit
from darkdetect import isDark
from qt_material import apply_stylesheet

darkTheme, lightTheme = 'dark_blue.xml', 'light_blue.xml'
size = 600, 400

class GUI:
    def __init__(self):
        self.app = QApplication(["app"])
        self.mainWindow = QMainWindow()
        self.mainWindow.resize(*size)
        self.mainWin = QWidget()

        self.initUI()
        self.initMenubar()

        self.mainWindow.setCentralWidget(self.mainWin)
        self.mainWindow.show()
        exit(self.app.exec_())


    def initUI(self):
        vLayout = QVBoxLayout()
        
        self.mainEntry = QLineEdit()
        vLayout.addWidget(self.mainEntry)

        self.buttonsWid = QWidget()
        gridLayout = QGridLayout()
        self.buttonsWid.setLayout(gridLayout)

        self.buttonText = [['9', '8', '7', '*'], ['6', '5', '4', '+'], ['3', '2', '1', '-'], ['0', 'Ans', 'C', '/']]
        self.buttons = []

        for i in range(4):
            self.buttons.append([])

            for j in range(4):
                self.buttons[i].append(QPushButton(self.buttonText[i][j]))
                self.buttons[i][j].clicked.connect(lambda _, i = i, j = j: self.onPress(i, j))
                gridLayout.addWidget(self.buttons[i][j], i, j)

        vLayout.addWidget(self.buttonsWid)
        self.mainWin.setLayout(vLayout)

    def initMenubar(self):
        global darkTheme, lightTheme
        if isDark():
            self.setTheme(darkTheme)
        else:
            self.setTheme(lightTheme)

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

    def setTheme(self, theme):
        apply_stylesheet(self.app, theme)

    def onPress(self, i, j):
        if i == 3 and j == 1:
            self.mainEntry.setText(str(eval(self.mainEntry.text())))
        elif i == 3 and j == 2:
            self.mainEntry.setText("")
        else: 
            self.mainEntry.setText(self.mainEntry.text() + self.buttonText[i][j])

if __name__ == "__main__":
    gui = GUI()