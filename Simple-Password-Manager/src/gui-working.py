from Working import Working
from PyQt5.QtWidgets import *
from sys import argv, exit
import qdarkstyle

class GUI:
    def __init__(self):
        self.app = QApplication(["Simple-Password-Manager-Working"])
        self.app.setStyleSheet(qdarkstyle.load_stylesheet())
        self.mainWin = QWidget()
        self.mainWinLayout = QHBoxLayout()
        self.mainWin.setLayout(self.mainWinLayout)

        self.initWorking()
        self.initUI()

        self.mainWin.show()
        exit(self.app.exec_())

    def initWorking(self):
        self.i = 0
        self.isOpen = True
        self.working = None

    def initUI(self):
        self.loginPage = QWidget()
        self.workingPage = QWidget()
        self.changePasswordPage = QWidget()

        self.initLoginPage()
        self.initWorkingPage()
        self.initChangePasswordPage()

        self.mainWinLayout.addWidget(self.loginPage)
        self.mainWinLayout.addWidget(self.workingPage)
        self.mainWinLayout.addWidget(self.changePasswordPage)

        self.workingPage.hide()
        self.changePasswordPage.hide()

    def initLoginPage(self):
        
        layout = QVBoxLayout()
        self.loginPage.setLayout(layout)
        
        entWid = QWidget()
        hLayout = QHBoxLayout()
        entWid.setLayout(hLayout)

        lab = QLabel(text = "Enter password: ")
        lab.adjustSize()
        hLayout.addWidget(lab)
        self.passIn = QLineEdit()
        hLayout.addWidget(self.passIn)
        
        layout.addWidget(entWid)
        # Entering entWid. 

        entWid1 = QWidget()
        vLayout = QVBoxLayout()
        entWid1.setLayout(vLayout)

        self.isPassCorrectLabel = QLabel(text = "")
        vLayout.addWidget(self.isPassCorrectLabel)
        self.checkPassword = QPushButton(text = "Check Password")
        self.checkPassword.clicked.connect(self.checkLogin)
        vLayout.addWidget(self.checkPassword)

        layout.addWidget(entWid1)

        self.mainWinLayout.addWidget(self.loginPage)

    def initWorkingPage(self):
        vLayout = QVBoxLayout()
        self.workingPage.setLayout(vLayout)
        self.workingPagePanel0 = QWidget()
        vLayout.addWidget(self.workingPagePanel0)
        
        workingPagePanel1 = QWidget()
        gridLayout = QGridLayout()
        workingPagePanel1.setLayout(gridLayout)

        # Making buttons. 
        getEntryButton = QPushButton(text = "Get Entry")
        seeEntriesButton = QPushButton(text = "See Entries")
        putEntryButton = QPushButton(text = "Put Entry")
        updateEntryButton = QPushButton(text = "Update Entry")
        changePrimaryPasswordButton = QPushButton(text = "Change Primary Password")

        # Adding functions to buttons.
        getEntryButton.clicked.connect(self.getEntry)
        seeEntriesButton.clicked.connect(self.seeEntries)
        putEntryButton.clicked.connect(self.putEntry)
        updateEntryButton.clicked.connect(self.updateEntry)
        changePrimaryPasswordButton.clicked.connect(self.changePrimaryPassword)

        # Adding buttons to panel1
        gridLayout.addWidget(getEntryButton, 0, 0)
        gridLayout.addWidget(seeEntriesButton, 0, 1)
        gridLayout.addWidget(putEntryButton, 0, 2)
        gridLayout.addWidget(updateEntryButton, 1, 0)
        gridLayout.addWidget(changePrimaryPasswordButton, 1, 1)

        vLayout.addWidget(workingPagePanel1)

    def initChangePasswordPage(self):
        vLayout = QVBoxLayout()
        self.changePasswordPage.setLayout(vLayout)

        # Making the grid Layout for gridWid that comes first in change password.
        gridWid = QWidget()
        gridLayout = QGridLayout()
        gridWid.setLayout(gridLayout)
        
        lab1 = QLabel("Enter Current Password:") 
        gridLayout.addWidget(lab1, 0, 0)

        self.oldPassEntry = QLineEdit()
        gridLayout.addWidget(self.oldPassEntry, 0, 1)

        lab2 = QLabel("Enter New Password:")
        gridLayout.addWidget(lab2, 1, 0)
        
        self.newPassEntry = QLineEdit()
        gridLayout.addWidget(self.newPassEntry, 1, 1)

        lab3 = QLabel("Confirm New Password:")
        gridLayout.addWidget(lab3, 2, 0)

        self.confirmNewPassEntry = QLineEdit()
        gridLayout.addWidget(self.confirmNewPassEntry, 2, 1)

        # Adding grid wid to change password page.
        vLayout.addWidget(gridWid)

        self.errorLabelinChangePasswordPage = QLabel()
        vLayout.addWidget(self.errorLabelinChangePasswordPage)

        hWid = QWidget()
        hLayout = QHBoxLayout()
        hWid.setLayout(hLayout)        
        
        goBack = QPushButton(text = "Go Back")
        funForThis = (lambda : self.goBackFunction(self.changePasswordPage))
        goBack.clicked.connect(funForThis)
        hLayout.addWidget(goBack)

        changePasswordButton = QPushButton(text = "Change Password")
        changePasswordButton.clicked.connect(self.tryChangePassword)
        hLayout.addWidget(changePasswordButton)

        vLayout.addWidget(hWid)

    def checkLogin(self):
        self.working = Working(self.passIn.text())
        
        if self.working.didPassWork():
            self.loginPage.hide()
            self.workingPage.show()
        else:
            self.isPassCorrectLabel.setText("Password Not correct. Try Again.")
            self.isPassCorrectLabel.adjustSize()
            self.working = None
            

    def getEntry(self):
        pass

    def seeEntries(self):
        pass 

    def putEntry(self):
        pass

    def updateEntry(self):
        pass

    def changePrimaryPassword(self):
        self.workingPage.hide()
        self.changePasswordPage.show()

    def goBackFunction(self, widgetToRemove):
        self.changePasswordPage.hide()
        self.workingPage.show()

    def tryChangePassword(self):
        oldPasStr = self.oldPassEntry.text()
        newPassStr = self.newPassEntry.text()   
        confirmPassStr = self.confirmNewPassEntry.text()

        if newPassStr != confirmPassStr:
            self.errorLabelinChangePasswordPage.setText("Passwords do not match")
            self.errorLabelinChangePasswordPage.adjustSize()
        else:
            didPassChange = self.working.changeMasterPassword(oldPasStr, newPassStr)
            if didPassChange:
                self.errorLabelinChangePasswordPage.setText("")
                self.errorLabelinChangePasswordPage.adjustSize()
                self.changePasswordPage.hide()
                self.workingPage.show()
            else:
                self.errorLabelinChangePasswordPage.setText("Old password was wrong. Password not changeed.")
                self.errorLabelinChangePasswordPage.adjustSize()

if __name__ == "__main__":
    gui = GUI()