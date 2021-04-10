# Import statements
from PyQt5.QtWidgets import *
from sys import exit
from qt_material import apply_stylesheet
from darkdetect import isDark
from random import randint

darkTheme, lightTheme = 'dark_blue.xml', 'light_blue.xml'

class GUI:
    def __init__(self):
        self.app = QApplication(["Tic-Tac-Toe"])
        self.mainWindow = QMainWindow()
        self.win = QWidget()
        self.mainWindow.setCentralWidget(self.win)

        self.initGamePlay()
        self.initMenuBar()
        self.initUI()

        self.mainWindow.show()
        exit(self.app.exec_())

    def initGamePlay(self):
        self.isOnePlayerGame = False
        self.curTurn = 'x'
        self.movesMade = 0
        self.curGame = [['' for i in range(3)] for j in range(3)]
        self.canPress = [[True for i in range(3)] for j in range(3)]

    def makeOnePlayerMove(self):
        while True:
            i, j = randint(0, 2), randint(0, 2)
            if self.curGame[i][j] == '':
                return i, j

    def initMenuBar(self):
        global darkTheme, lightTheme

        self.menuBar = QMenuBar()

        self.themeMenu = QMenu("Theme Menu")
        self.lightThemeAction = QAction("Light Theme")
        self.lightThemeAction.triggered.connect(lambda : apply_stylesheet(self.app, lightTheme))
        self.themeMenu.addAction(self.lightThemeAction)
        self.darkThemeAction = QAction("Dark Theme")
        self.darkThemeAction.triggered.connect(lambda : apply_stylesheet(self.app, darkTheme))
        self.themeMenu.addAction(self.darkThemeAction)
        self.menuBar.addMenu(self.themeMenu)

        self.gameMenu = QMenu("New Game")
        self.makeNewOnePlayerGameAction = QAction("New 1 player game.")
        self.makeNewOnePlayerGameAction.triggered.connect(lambda : self.makeNewOnePlayerGame())
        self.gameMenu.addAction(self.makeNewOnePlayerGameAction)
        self.makeNewTwoPlayerGameAction = QAction("New 2 player game.")
        self.makeNewTwoPlayerGameAction.triggered.connect(lambda : self.makeNewTwoPlayerGame())
        self.gameMenu.addAction(self.makeNewTwoPlayerGameAction)
        self.menuBar.addMenu(self.gameMenu)

        self.mainWindow.setMenuBar(self.menuBar)

    def makeNewGame(self):
        self.movesMade = 0
        self.lab.setText('')
        for i in range(3):
            for j in range(3):
                self.curGame[i][j] = ''
                self.buttons[i][j].setText('')
                self.canPress[i][j] = True
        self.curTurn = 'x'

    def makeNewTwoPlayerGame(self):
        self.isOnePlayerGame = False
        self.makeNewGame()

    def makeNewOnePlayerGame(self):
        self.isOnePlayerGame = True
        self.makeNewGame()

    def initUI(self):
        global darkTheme, lightTheme
        if isDark():
            apply_stylesheet(self.app, darkTheme)
        else:
            apply_stylesheet(self.app, lightTheme)

        self.lab = QLabel(text = "", parent=self.win)   
        self.lab.adjustSize() # It is a kind of better to do this to avoid bugs.

        self.wid = QWidget()

        vlayout = QVBoxLayout()
        self.win.setLayout(vlayout)
        vlayout.addWidget(self.lab)
        vlayout.addWidget(self.wid)

        # Making a widget to store buttons.
        layout = QGridLayout()
        self.wid.setLayout(layout)

        self.buttons = []

        for i in range(3):
            self.buttons.append([])
            for j in range(3):
                self.buttons[i].append(QPushButton())
                self.buttons[i][j].clicked.connect(lambda _, i = i, j = j: self.onPress(i, j))
                layout.addWidget(self.buttons[i][j], i, j)

    def onPress(self, i, j):
        if self.canPress[i][j]:
            self.buttons[i][j].setText(self.curTurn)
            self.curGame[i][j] = self.curTurn
            if self.didWinOccur():
                self.lab.setText("{} won".format(self.curTurn))
                for i in range(3):
                    for j in range(3):
                        self.canPress[i][j] = False
            if self.isOnePlayerGame:
                i, j = self.makeOnePlayerMove()
                self.canPress[i][j] = False
                self.buttons[i][j].setText('o')
                self.curGame[i][j] = 'o'
                self.movesMade += 2
                self.curTurn = 'o'
                if self.didWinOccur():
                    self.lab.setText('o won')
                    for i in range(3):
                        for j in range(3):
                            self.canPress[i][j] = False
                else:
                    pass
                self.curTurn = 'x'
                if self.movesMade == 8:
                    for i in range(3):
                        for j in range(3):
                            if self.curGame[i][j] == '':
                                self.curGame[i][j] = 'x'
                    if self.didWinOccur():
                        self.lab.setText("X won.")
                    else:
                        self.lab.setText("Draw.")
                        for i in range(3):
                            for j in range(3):
                                self.canPress[i][j] = False
            else:    
                self.curTurn = 'o' if self.curTurn == 'x' else 'x'
                self.canPress[i][j] = False
                self.movesMade += 1

    def didWinOccur(self):
        if self.curGame[1][1] == self.curTurn:
            if self.curGame[0][0] == self.curTurn and self.curGame[2][2] == self.curTurn:
                return True
            if self.curGame[0][2] == self.curTurn and self.curGame[2][0] == self.curTurn:
                return True
            if self.curGame[1][0] == self.curTurn and self.curGame[1][2] == self.curTurn:
                return True
            if self.curGame[0][1] == self.curTurn and self.curGame[2][1] == self.curTurn:
                return True
        else:
            if self.curGame[0][0] == self.curTurn and self.curGame[0][1] == self.curTurn and self.curGame[0][2] == self.curTurn:
                return True
            if self.curGame[2][0] == self.curTurn and self.curGame[2][1] == self.curTurn and self.curGame[2][2] == self.curTurn:
                return True
            if self.curGame[0][0] == self.curTurn and self.curGame[1][0] == self.curTurn and self.curGame[2][0] == self.curTurn:
                return True
            if self.curGame[0][2] == self.curTurn and self.curGame[1][2] == self.curTurn and self.curGame[2][2] == self.curTurn:
                return True
        return False