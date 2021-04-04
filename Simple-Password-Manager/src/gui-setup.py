from setup import setup
from PyQt5.QtWidgets import *
from sys import exit
from qt_material import apply_stylesheet

darkTheme, lightTheme = 'dark_cyan.xml', 'light_blue.xml'

class GUI:
    def __init__(self):
        self.app = QApplication(["Simple-Password-Manager-Setup"])
        # self.app.setStyleSheet()
        self.mainWindow = QMainWindow()
        self.win = QWidget()
        self.mainWindow.setCentralWidget(self.win)

        self.initUI()
        self.initMenuBar()

        self.mainWindow.show()
        exit(self.app.exec_())

    def initUI(self):
        self.setTheme(2)
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

    def initMenuBar(self):
        global darkTheme, lightTheme

        self.menuBar = QMenuBar()
        self.mainWindow.setMenuBar(self.menuBar)
        self.themeMenu = QMenu("theme menu", self.mainWindow)

        self.lightTheme = QAction("Light Theme", self.themeMenu)
        self.themeMenu.addAction(self.lightTheme)
        self.lightTheme.triggered.connect(lambda : self.setTheme(lightTheme))
        self.darkTheme = QAction("Dark Theme", self.themeMenu)
        self.themeMenu.addAction(self.darkTheme)
        self.darkTheme.triggered.connect(lambda : self.setTheme(darkTheme))

        self.menuBar.addMenu(self.themeMenu)

    def setTheme(self, theme):
        apply_stylesheet(self.app, theme)

if __name__ == "__main__":
    gui = GUI()