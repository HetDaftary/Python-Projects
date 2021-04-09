from src.Working import Working
from PyQt5.QtWidgets import *
from sys import exit
from clipboard import copy
from qt_material import apply_stylesheet
from darkdetect import isDark

size = 960, 540
darkTheme, lightTheme = 'dark_blue.xml', 'light_blue.xml'


class GUI:
    def __init__(self):
        self.app = QApplication(["Simple-Password-Manager-Working"])
        self.mainWindow = QMainWindow()
        self.mainWindow.resize(*size)
        self.mainWin = QWidget()
        self.mainWinLayout = QHBoxLayout()
        self.mainWin.setLayout(self.mainWinLayout)
        self.initWorking()
        self.initUI()

        self.mainWindow.setCentralWidget(self.mainWin)
        self.mainWindow.show()
        exit(self.app.exec_())

    def initWorking(self):
        global darkTheme, lightTheme
        self.working = None
        if isDark():
            self.setTheme(darkTheme)
        else:
            self.setTheme(lightTheme)

    def initUI(self):
        self.loginPage = QWidget()
        self.workingPage = QWidget()
        self.changePasswordPage = QWidget()
        self.getEntryPage = QWidget()
        self.seeEntriesPage = QWidget()
        self.putEntryPage = QWidget()
        self.updateEntryPage = QWidget()

        self.initLoginPage()
        self.initWorkingPage()
        self.initChangePasswordPage()
        self.initGetEntryPage()
        self.initSeeEntriesPage()
        self.initPutEntryPage()
        self.initUpdateEntryPage()
        self.initMenuBar()

        self.mainWinLayout.addWidget(self.loginPage)
        self.mainWinLayout.addWidget(self.workingPage)
        self.mainWinLayout.addWidget(self.changePasswordPage)
        self.mainWinLayout.addWidget(self.getEntryPage)
        self.mainWinLayout.addWidget(self.seeEntriesPage)
        self.mainWinLayout.addWidget(self.putEntryPage)
        self.mainWinLayout.addWidget(self.updateEntryPage)

        self.workingPage.hide()
        self.changePasswordPage.hide()
        self.getEntryPage.hide()
        self.seeEntriesPage.hide()
        self.putEntryPage.hide()
        self.updateEntryPage.hide()

    def initMenuBar(self):
        global darkTheme, lightTheme

        self.menuBar = QMenuBar()
        self.mainWindow.setMenuBar(self.menuBar)
        self.themeMenu = QMenu("theme menu", self.mainWindow)

        self.lightTheme = QAction("Light Theme", self.themeMenu)
        self.themeMenu.addAction(self.lightTheme)
        self.lightTheme.triggered.connect(lambda: self.setTheme(lightTheme))
        self.darkTheme = QAction("Dark Theme", self.themeMenu)
        self.themeMenu.addAction(self.darkTheme)
        self.darkTheme.triggered.connect(lambda: self.setTheme(darkTheme))

        self.menuBar.addMenu(self.themeMenu)

    def initLoginPage(self):

        layout = QVBoxLayout()
        self.loginPage.setLayout(layout)

        entWid = QWidget()
        hLayout = QHBoxLayout()
        entWid.setLayout(hLayout)

        lab = QLabel(text="Enter password: ")
        lab.adjustSize()
        hLayout.addWidget(lab)
        self.passIn = QLineEdit()
        self.passIn.setEchoMode(QLineEdit.Password)
        hLayout.addWidget(self.passIn)

        layout.addWidget(entWid)
        # Entering entWid.

        entWid1 = QWidget()
        vLayout = QVBoxLayout()
        entWid1.setLayout(vLayout)

        self.isPassCorrectLabel = QLabel(text="")
        vLayout.addWidget(self.isPassCorrectLabel)
        self.checkPassword = QPushButton(text="Check Password")
        self.checkPassword.clicked.connect(self.checkLogin)
        vLayout.addWidget(self.checkPassword)

        layout.addWidget(entWid1)

        self.mainWinLayout.addWidget(self.loginPage)

    def initWorkingPage(self):
        vLayout = QVBoxLayout()
        self.workingPage.setLayout(vLayout)
        workingPagePanel1 = QWidget()
        gridLayout = QGridLayout()
        workingPagePanel1.setLayout(gridLayout)

        # Making buttons.
        getEntryButton = QPushButton(text="Get Entry")
        seeEntriesButton = QPushButton(text="See Entries")
        putEntryButton = QPushButton(text="Put Entry")
        updateEntryButton = QPushButton(text="Update Entry")
        changePrimaryPasswordButton = QPushButton(text="Change Primary Password")

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
        self.newPassEntry.setEchoMode(QLineEdit.Password)
        gridLayout.addWidget(self.newPassEntry, 1, 1)

        lab3 = QLabel("Confirm New Password:")
        gridLayout.addWidget(lab3, 2, 0)

        self.confirmNewPassEntry = QLineEdit()
        self.confirmNewPassEntry.setEchoMode(QLineEdit.Password)
        gridLayout.addWidget(self.confirmNewPassEntry, 2, 1)

        # Adding grid wid to change password page.
        vLayout.addWidget(gridWid)

        self.errorLabelInChangePasswordPage = QLabel()
        vLayout.addWidget(self.errorLabelInChangePasswordPage)

        hWid = QWidget()
        hLayout = QHBoxLayout()
        hWid.setLayout(hLayout)

        goBack = QPushButton(text="Go Back")
        funForThis = (lambda: self.goBackFunction(self.changePasswordPage))
        goBack.clicked.connect(funForThis)
        hLayout.addWidget(goBack)

        changePasswordButton = QPushButton(text="Change Password")
        changePasswordButton.clicked.connect(self.tryChangePassword)
        hLayout.addWidget(changePasswordButton)

        vLayout.addWidget(hWid)

    def initGetEntryPage(self):
        vLayout = QVBoxLayout()
        self.getEntryPage.setLayout(vLayout)
        # Setting Layout

        wid1 = QWidget()
        gridLayout = QGridLayout()
        wid1.setLayout(gridLayout)
        lab1 = QLabel("Enter Website:")
        gridLayout.addWidget(lab1, 0, 0)
        self.getEntryPageWebsiteEntry = QLineEdit()
        gridLayout.addWidget(self.getEntryPageWebsiteEntry, 0, 1)
        lab2 = QLabel("Enter E-mail:")
        gridLayout.addWidget(lab2, 1, 0)
        self.getEntryPageEmailEntry = QLineEdit()
        gridLayout.addWidget(self.getEntryPageEmailEntry, 1, 1)

        vLayout.addWidget(wid1)

        self.errorsInGetEntryLabel = QLabel()
        vLayout.addWidget(self.errorsInGetEntryLabel)

        wid2 = QWidget()
        hLayout = QHBoxLayout()
        wid2.setLayout(hLayout)

        goBackButton = QPushButton(text="Go Back")
        goBackButton.clicked.connect(lambda: self.goBackFunction(self.getEntryPage))
        hLayout.addWidget(goBackButton)

        getPasswordButton = QPushButton(text="Get Password")
        getPasswordButton.clicked.connect(
            lambda: self.getPasswordGetEntry(self.getEntryPageWebsiteEntry.text(), self.getEntryPageEmailEntry.text()))
        hLayout.addWidget(getPasswordButton)
        vLayout.addWidget(wid2)

    def initSeeEntriesPage(self):
        vLayout = QVBoxLayout()
        self.seeEntriesPage.setLayout(vLayout)

        self.placeToPutEntries = QWidget()
        self.placeToPutEntriesLayout = QGridLayout()
        self.placeToPutEntries.setLayout(self.placeToPutEntriesLayout)
        vLayout.addWidget(self.placeToPutEntries)

        goBackButton = QPushButton("Go back")
        goBackButton.clicked.connect(lambda: self.goBackFunction(self.seeEntriesPage))
        vLayout.addWidget(goBackButton)

    def initPutEntryPage(self):
        vLayout = QVBoxLayout()
        self.putEntryPage.setLayout(vLayout)

        wid1 = QWidget()
        gridLayout = QGridLayout()
        wid1.setLayout(gridLayout)

        lab1 = QLabel("Website:")
        gridLayout.addWidget(lab1, 0, 0)
        self.putEntryWebsiteEntry = QLineEdit()
        gridLayout.addWidget(self.putEntryWebsiteEntry, 0, 1)

        lab2 = QLabel("Email:")
        gridLayout.addWidget(lab2, 1, 0)
        self.putEntryEmailEntry = QLineEdit()
        gridLayout.addWidget(self.putEntryEmailEntry, 1, 1)

        lab3 = QLabel("Password:")
        gridLayout.addWidget(lab3, 2, 0)
        self.putEntryPasswordEntry = QLineEdit()
        self.putEntryPasswordEntry.setEchoMode(QLineEdit.Password)
        gridLayout.addWidget(self.putEntryPasswordEntry)

        vLayout.addWidget(wid1)

        self.errorsInPutEntry = QLabel("")
        vLayout.addWidget(self.errorsInPutEntry)

        wid2 = QWidget()
        hLayout = QHBoxLayout()
        wid2.setLayout(hLayout)

        goBackButton = QPushButton("Go back")
        goBackButton.clicked.connect(lambda: self.goBackFunction(self.putEntryPage))
        hLayout.addWidget(goBackButton)

        putEntryButton = QPushButton("Put Entry")
        putEntryButton.clicked.connect(self.putEntryFunction)
        hLayout.addWidget(putEntryButton)

        vLayout.addWidget(wid2)

    def initUpdateEntryPage(self):
        vLayout = QVBoxLayout()
        self.updateEntryPage.setLayout(vLayout)

        wid1 = QWidget()
        gridLayout = QGridLayout()
        wid1.setLayout(gridLayout)

        lab1 = QLabel("Enter old Website:")
        gridLayout.addWidget(lab1, 0, 0)
        self.updateEntryOldWebsiteEntry = QLineEdit()
        gridLayout.addWidget(self.updateEntryOldWebsiteEntry, 0, 1)
        lab2 = QLabel("Enter old email:")
        gridLayout.addWidget(lab2, 1, 0)
        self.updateEntryOldEmailEntry = QLineEdit()
        gridLayout.addWidget(self.updateEntryOldEmailEntry, 1, 1)
        lab3 = QLabel("Enter new Website:")
        gridLayout.addWidget(lab3, 2, 0)
        self.updateEntryNewWebsiteEntry = QLineEdit()
        gridLayout.addWidget(self.updateEntryNewWebsiteEntry, 2, 1)
        lab4 = QLabel("Enter new email:")
        gridLayout.addWidget(lab4, 3, 0)
        self.updateEntryNewEmailEntry = QLineEdit()
        gridLayout.addWidget(self.updateEntryNewEmailEntry, 3, 1)
        lab5 = QLabel("Enter new password:")
        gridLayout.addWidget(lab5, 4, 0)
        self.updateEntryNewPasswordEntry = QLineEdit()
        self.updateEntryNewPasswordEntry.setEchoMode(QLineEdit.Password)
        gridLayout.addWidget(self.updateEntryNewPasswordEntry, 4, 1)

        vLayout.addWidget(wid1)

        self.errorsInUpdateEntry = QLabel()
        vLayout.addWidget(self.errorsInUpdateEntry)

        wid2 = QWidget()
        hLayout = QHBoxLayout()
        wid2.setLayout(hLayout)

        goBackButton = QPushButton("Go back")
        goBackButton.clicked.connect(lambda: self.goBackFunction(self.updateEntryPage))
        hLayout.addWidget(goBackButton)

        updateEntryButton = QPushButton("Update Entry")
        updateEntryButton.clicked.connect(self.updateEntryFunction)
        hLayout.addWidget(updateEntryButton)

        vLayout.addWidget(wid2)

    def checkLogin(self):
        self.working = Working(self.passIn.text())

        if self.working.didPassWork():
            self.loginPage.hide()
            self.workingPage.show()
        else:
            self.isPassCorrectLabel.setText("Password Not correct. Try Again.")
            self.isPassCorrectLabel.adjustSize()
            self.working = None

    def cleanAWidget(self, layoutToClean):
        for i in reversed(range(layoutToClean.count())):
            layoutToClean.itemAt(i).widget().setParent(None)

    def getEntry(self):
        self.getEntryPageEmailEntry.setText("")
        self.getEntryPageWebsiteEntry.setText("")
        self.errorsInGetEntryLabel.setText("")
        self.errorsInGetEntryLabel.adjustSize()
        self.workingPage.hide()
        self.getEntryPage.show()

    def seeEntries(self):
        self.currentEntries = self.working.seeEntries()

        self.cleanAWidget(self.placeToPutEntriesLayout)

        self.placeToPutEntriesLayout.addWidget(QLabel("Email"), 0, 0)
        self.placeToPutEntriesLayout.addWidget(QLabel("Website"), 0, 1)
        self.placeToPutEntriesLayout.addWidget(QLabel(""), 0, 2)
        self.placeToPutEntriesLayout.addWidget(QLabel(""), 0, 3)

        count = 1

        for i in range(len(self.currentEntries)):
            countV = 0
            for j in self.currentEntries[i]:
                self.placeToPutEntriesLayout.addWidget(QLabel(text=j), count, countV)
                # print(count, countV)
                countV += 1

            currentButton = QPushButton("Get this Entry")
            currentButton.clicked.connect(lambda _, a=i: self.getPasswordFromButton(self.currentEntries[a]))
            self.placeToPutEntriesLayout.addWidget(currentButton, count, countV)
            countV += 1

            currentUpdateButton = QPushButton("Update this Entry")
            currentUpdateButton.clicked.connect(lambda _, a=i: self.updateEntryFromSeeEntries(self.currentEntries[a]))
            self.placeToPutEntriesLayout.addWidget(currentUpdateButton, count, countV)

            count += 1

        self.workingPage.hide()
        self.seeEntriesPage.show()

    def putEntry(self):
        self.putEntryWebsiteEntry.setText("")
        self.putEntryEmailEntry.setText("")
        self.putEntryPasswordEntry.setText("")
        self.errorsInPutEntry.setText("")
        self.errorsInPutEntry.adjustSize()
        self.workingPage.hide()
        self.putEntryPage.show()

    def updateEntry(self):
        self.updateEntryOldWebsiteEntry.setText("")
        self.updateEntryOldEmailEntry.setText("")
        self.updateEntryNewWebsiteEntry.setText("")
        self.updateEntryNewEmailEntry.setText("")
        self.updateEntryNewPasswordEntry.setText("")
        self.errorsInUpdateEntry.setText("")
        self.errorsInUpdateEntry.adjustSize()
        self.workingPage.hide()
        self.updateEntryPage.show()

    def changePrimaryPassword(self):
        self.errorLabelInChangePasswordPage.setText("")
        self.errorLabelInChangePasswordPage.adjustSize()
        self.workingPage.hide()
        self.changePasswordPage.show()

    def goBackFunction(self, widgetToRemove):
        widgetToRemove.hide()
        self.workingPage.show()

    def tryChangePassword(self):
        oldPasStr = self.oldPassEntry.text()
        newPassStr = self.newPassEntry.text()
        confirmPassStr = self.confirmNewPassEntry.text()

        if newPassStr != confirmPassStr:
            self.errorLabelInChangePasswordPage.setText("Passwords do not match")
            self.errorLabelInChangePasswordPage.adjustSize()
        else:
            didPassChange = self.working.changeMasterPassword(oldPasStr, newPassStr)
            if didPassChange:
                self.errorLabelInChangePasswordPage.setText("")
                self.errorLabelInChangePasswordPage.adjustSize()
                self.changePasswordPage.hide()
                self.workingPage.show()
            else:
                self.errorLabelInChangePasswordPage.setText("Old password was wrong. Password not changed.")
                self.errorLabelInChangePasswordPage.adjustSize()

    def getPasswordGetEntry(self, website, email):
        try:
            self.getPassword(website, email)
            self.errorsInGetEntryLabel.setText("Got the password. Copied to Clipboard")
            self.errorsInGetEntryLabel.adjustSize()
        except:
            self.errorsInGetEntryLabel.setText("Record does not exist.")
            self.errorsInGetEntryLabel.adjustSize()

    def updateEntryFromSeeEntries(self, toGet):
        self.updateEntryOldEmailEntry.setText(toGet[0])
        self.updateEntryOldWebsiteEntry.setText(toGet[1])
        self.updateEntryNewEmailEntry.setText("")
        self.updateEntryNewWebsiteEntry.setText("")
        self.updateEntryNewPasswordEntry.setText("")

        self.seeEntriesPage.hide()
        self.updateEntryPage.show()

    def getPasswordFromButton(self, toGet):
        self.getPassword(toGet[1], toGet[0])

    def getPassword(self, website, email):
        copy(self.working.getEntry(email, website))

    def putEntryFunction(self):
        try:
            web = self.putEntryWebsiteEntry.text()
            email = self.putEntryEmailEntry.text()
            password = self.putEntryPasswordEntry.text()
            self.working.putEntry(email, web, password)
            self.errorsInPutEntry.setText("Registered.")
            self.errorsInPutEntry.adjustSize()
            self.errorsInPutEntry.adjustSize()
        except:
            self.errorsInPutEntry.setText("Error.")
            self.errorsInPutEntry.adjustSize()

    def updateEntryFunction(self):
        try:
            email = self.updateEntryOldEmailEntry.text()
            website = self.updateEntryOldWebsiteEntry.text()
            newEmail = self.updateEntryNewEmailEntry.text()
            newWebsite = self.updateEntryNewWebsiteEntry.text()
            newPassword = self.updateEntryNewPasswordEntry.text()
            self.working.updateEntry(email, website, newEmail, newWebsite, newPassword)
            self.errorsInUpdateEntry.setText("Updated.")
            self.errorsInUpdateEntry.adjustSize()
        except:
            self.errorsInUpdateEntry.setText("Error.")
            self.errorsInUpdateEntry.adjustSize()

    def setTheme(self, theme):
        apply_stylesheet(self.app, theme)