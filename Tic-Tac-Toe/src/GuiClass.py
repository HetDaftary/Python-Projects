# Import statements
from PyQt5.QtWidgets import *
from sys import exit
import qdarkstyle
# import breeze_resources


class GUI:
    def __init__(self):
        self.app = QApplication(["Tic-Tac-Toe"])
        self.app.setStyleSheet(qdarkstyle.load_stylesheet())

        self.win = QWidget()
        
        self.initGamePlay()
        self.initUI()

        self.win.show()
        exit(self.app.exec_())

    def initGamePlay(self):
        self.curTurn = 'x'
        self.curGame = [['' for i in range(3)] for j in range(3)]
        self.canPress = [[True for i in range(3)] for j in range(3)]

    def initUI(self):
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

        b00 = QPushButton(text = "")
        b01 = QPushButton(text = "")
        b02 = QPushButton(text = "")
        
        b10 = QPushButton(text = "")
        b11 = QPushButton(text = "")
        b12 = QPushButton(text = "")
        
        b20 = QPushButton(text = "")
        b21 = QPushButton(text = "")
        b22 = QPushButton(text = "")
        
        layout.addWidget(b00, 0, 0)
        layout.addWidget(b01, 0, 1)
        layout.addWidget(b02, 0, 2)
        
        layout.addWidget(b10, 1, 0)
        layout.addWidget(b11, 1, 1)
        layout.addWidget(b12, 1, 2)
        
        layout.addWidget(b20, 2, 0)
        layout.addWidget(b21, 2, 1)
        layout.addWidget(b22, 2, 2)

        b00.clicked.connect(lambda : self.onPress(0, 0))
        b01.clicked.connect(lambda : self.onPress(0, 1))
        b02.clicked.connect(lambda : self.onPress(0, 2))

        b10.clicked.connect(lambda : self.onPress(1, 0))
        b11.clicked.connect(lambda : self.onPress(1, 1))
        b12.clicked.connect(lambda : self.onPress(1, 2))
        
        b20.clicked.connect(lambda : self.onPress(2, 0))
        b21.clicked.connect(lambda : self.onPress(2, 1))
        b22.clicked.connect(lambda : self.onPress(2, 2))

        self.buttons = [[b00, b01, b02], [b10, b11, b12], [b20, b21, b22]]

    def onPress(self, i, j):
        if self.canPress[i][j]:
            self.buttons[i][j].setText(self.curTurn)
            self.curGame[i][j] = self.curTurn
            if self.didWinOccur():
                self.lab.setText("{} won".format(self.curTurn))
                for i in range(3):
                    for j in range(3):
                        self.canPress[i][j] = False
            self.curTurn = 'o' if self.curTurn == 'x' else 'x'
            self.canPress[i][j] = False

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