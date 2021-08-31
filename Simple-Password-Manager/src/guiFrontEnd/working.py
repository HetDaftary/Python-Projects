from src.working.setup import fileName
from src.working import Working
from PyQt5 import QtWidgets as qtw
from typing import *
from clipboard import copy
import sys
from qt_material import apply_stylesheet
from darkdetect import isDark

size = 960, 540
darkTheme, lightTheme = 'dark_blue.xml', 'light_blue.xml'
styleNames = ["OS preferred", "light Theme", "dark theme"]

def updateQLabel(label: qtw.QLabel, text: str) -> None: 
    label.setText(text)
    label.adjustSize()

class WorkingPage(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        gridLayout = qtw.QGridLayout()
        self.setLayout(gridLayout)

        self.goToGetEntryPage =  qtw.QPushButton("Get Entry")
        gridLayout.addWidget(self.goToGetEntryPage, 0, 0)

        self.goToPutEntryPage = qtw.QPushButton("Put Entry")
        gridLayout.addWidget(self.goToPutEntryPage, 0, 1)

        self.goToSeeEntriesPage = qtw.QPushButton("See Entries")
        gridLayout.addWidget(self.goToSeeEntriesPage, 0, 2)

        self.goToUpdateEntryPage = qtw.QPushButton("Update Entry")
        gridLayout.addWidget(self.goToUpdateEntryPage, 1, 0)

        self.goToChangePrimaryPasswordPage = qtw.QPushButton("Change Primary Password")
        gridLayout.addWidget(self.goToChangePrimaryPasswordPage, 1, 1)

        self.logoutButton = qtw.QPushButton("Logout")
        gridLayout.addWidget(self.logoutButton, 1, 2)

class LoginPage(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):
        vBoxLayout = qtw.QVBoxLayout()
        self.setLayout(vBoxLayout)

        hBoxWidget = qtw.QWidget()
        hBoxLayout = qtw.QHBoxLayout()
        hBoxWidget.setLayout(hBoxLayout)

        askForPasswordLabel = qtw.QLabel("Password: ")
        hBoxLayout.addWidget(askForPasswordLabel)
        self.passwordLineEdit = qtw.QLineEdit()
        hBoxLayout.addWidget(self.passwordLineEdit)
        self.passwordLineEdit.setEchoMode(qtw.QLineEdit.Password)

        vBoxLayout.addWidget(hBoxWidget)

        self.statusLine = qtw.QLabel("")
        vBoxLayout.addWidget(self.statusLine)

        self.loginButton = qtw.QPushButton("Login")
        vBoxLayout.addWidget(self.loginButton)

class SeeEntries(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        vBoxLayout = qtw.QVBoxLayout()
        self.setLayout(vBoxLayout)

        gridWidget = qtw.QWidget()
        self.gridLayout = qtw.QGridLayout()
        gridWidget.setLayout(self.gridLayout)

        vBoxLayout.addWidget(gridWidget)

        self.goBackButton = qtw.QPushButton("Go Back")
        vBoxLayout.addWidget(self.goBackButton)
    
class TemplateClass(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()

        vBoxLayout = qtw.QVBoxLayout()
        self.setLayout(vBoxLayout)

        gridWidget = qtw.QWidget()
        self.gridLayout = qtw.QGridLayout()
        gridWidget.setLayout(self.gridLayout)
        vBoxLayout.addWidget(gridWidget)

        self.statusLine = qtw.QLabel("")
        vBoxLayout.addWidget(self.statusLine)

        hBoxWidget = qtw.QWidget()
        hBoxLayout = qtw.QHBoxLayout()
        hBoxWidget.setLayout(hBoxLayout)
        
        self.goBackButton = qtw.QPushButton("Go Back")
        hBoxLayout.addWidget(self.goBackButton)

        self.doActionButton = qtw.QPushButton("")
        hBoxLayout.addWidget(self.doActionButton)

        vBoxLayout.addWidget(hBoxWidget)

class GetEntry(TemplateClass):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):
        websiteLabel = qtw.QLabel("Website: ")
        self.gridLayout.addWidget(websiteLabel, 0, 0)
        self.websiteLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.websiteLineEdit, 0, 1)

        emailLabel = qtw.QLabel("Email: ")
        self.gridLayout.addWidget(emailLabel, 1, 0)
        self.emailLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.emailLineEdit, 1, 1)

        self.doActionButton.setText("Get Entry")

class PutEntry(TemplateClass):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        websiteLabel = qtw.QLabel("Website: ")
        self.gridLayout.addWidget(websiteLabel, 0, 0)
        self.websiteLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.websiteLineEdit, 0, 1)

        emailLabel = qtw.QLabel("Email: ")
        self.gridLayout.addWidget(emailLabel, 1, 0)
        self.emailLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.emailLineEdit, 1, 1)

        passwordLabel = qtw.QLabel("Password: ")
        self.gridLayout.addWidget(passwordLabel, 2, 0)
        self.passwordLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.passwordLineEdit, 2, 1)
        self.passwordLineEdit.setEchoMode(qtw.QLineEdit.Password)

        self.doActionButton.setText("Put Entry")

class UpdateEntry(TemplateClass):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):
        oldWebsiteLabel = qtw.QLabel("Old Website: ")
        self.gridLayout.addWidget(oldWebsiteLabel, 0, 0)
        self.oldWebsiteLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.oldWebsiteLineEdit, 0, 1)

        oldEmailLabel = qtw.QLabel("Old Email: ")
        self.gridLayout.addWidget(oldEmailLabel, 1, 0)
        self.oldEmailLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.oldEmailLineEdit, 1, 1)

        websiteLabel = qtw.QLabel("Website: ")
        self.gridLayout.addWidget(websiteLabel, 2, 0)
        self.websiteLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.websiteLineEdit, 2, 1)

        emailLabel = qtw.QLabel("Email: ")
        self.gridLayout.addWidget(emailLabel, 3, 0)
        self.emailLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.emailLineEdit, 3, 1)

        passwordLabel = qtw.QLabel("Password: ")
        self.gridLayout.addWidget(passwordLabel, 4, 0)
        self.passwordLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.passwordLineEdit, 4, 1)
        self.passwordLineEdit.setEchoMode(qtw.QLineEdit.Password)

        self.doActionButton.setText("Update Entry")

class ChangePrimaryPassword(TemplateClass):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        oldPasswordLabel = qtw.QLabel("Old Password: ")
        self.gridLayout.addWidget(oldPasswordLabel, 0, 0)
        self.oldPasswordLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.oldPasswordLineEdit, 0, 1)
        self.oldPasswordLineEdit.setEchoMode(qtw.QLineEdit.Password)

        newPasswordLabel = qtw.QLabel("New Password: ")
        self.gridLayout.addWidget(newPasswordLabel, 1, 0)
        self.newPasswordLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.newPasswordLineEdit, 1, 1)
        self.newPasswordLineEdit.setEchoMode(qtw.QLineEdit.Password)

        self.confirmNewPasswordLabel = qtw.QLabel("Confirm New Password: ")
        self.gridLayout.addWidget(self.confirmNewPasswordLabel, 2, 0)
        self.confirmNewPasswordLineEdit = qtw.QLineEdit()
        self.gridLayout.addWidget(self.confirmNewPasswordLineEdit, 2, 1)
        self.confirmNewPasswordLineEdit.setEchoMode(qtw.QLineEdit.Password)

        self.doActionButton.setText("Change Password")

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initMenuBar()

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

    def initUI(self):
        global size
        self.resize(*size)

        self.mainWin = qtw.QWidget()
        mainWinLayout = qtw.QVBoxLayout()
        self.mainWin.setLayout(mainWinLayout)
        self.setCentralWidget(self.mainWin)

        self.loginPage = LoginPage()
        self.seeEntriesPage = SeeEntries()
        self.updateEntryPage = UpdateEntry()
        self.changePrimaryPasswordPage = ChangePrimaryPassword()
        self.putEntryPage = PutEntry()
        self.getEntryPage = GetEntry()
        self.workingPage = WorkingPage()

        mainWinLayout.addWidget(self.loginPage)
        mainWinLayout.addWidget(self.workingPage)
        mainWinLayout.addWidget(self.seeEntriesPage)
        mainWinLayout.addWidget(self.updateEntryPage)
        mainWinLayout.addWidget(self.changePrimaryPasswordPage)
        mainWinLayout.addWidget(self.putEntryPage)
        mainWinLayout.addWidget(self.getEntryPage)

        self.workingPage.hide()
        self.changePrimaryPasswordPage.hide()
        self.putEntryPage.hide()
        self.getEntryPage.hide()
        self.updateEntryPage.hide()
        self.seeEntriesPage.hide()

        self.show()

class GUI(qtw.QApplication):
    def __init__(self):
        super().__init__(["Simple Password Manager"])

        self.mainWindow = MainWindow()

        self.initWorking()
        self.initButtonActions()
        self.initMenuActions()

        sys.exit(self.exec_())

    def initWorking(self):
        self.working = None 
        self.currentStyle = 0
        self.changeStyle(self.mainWindow.osPreferredTheme)

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

    def initMenuActions(self):
        self.mainWindow.osPreferredTheme.triggered.connect(lambda: self.changeStyle(self.mainWindow.osPreferredTheme))
        self.mainWindow.lightTheme.triggered.connect(lambda: self.changeStyle(self.mainWindow.lightTheme))
        self.mainWindow.darkTheme.triggered.connect(lambda: self.changeStyle(self.mainWindow.darkTheme))
    
    def initButtonActions(self):
        self.mainWindow.loginPage.loginButton.clicked.connect(self.checkLogin)
        
        # Working Page Buttons.
        workingPage = self.mainWindow.workingPage
        workingPage.goToGetEntryPage.clicked.connect(self.goToGetEntryPageFunction)
        workingPage.goToPutEntryPage.clicked.connect(self.goToPutEntryPageFunction)
        workingPage.goToChangePrimaryPasswordPage.clicked.connect(self.goToChangePrimaryPasswordPageFunction)
        workingPage.goToSeeEntriesPage.clicked.connect(self.goToSeeEntriesPageFunction)
        workingPage.goToUpdateEntryPage.clicked.connect(self.goToUpdateEntryPageFunction)
        workingPage.logoutButton.clicked.connect(self.logoutFunction)

        # Put Entry Page Buttons.
        putEntryPage = self.mainWindow.putEntryPage
        putEntryPage.doActionButton.clicked.connect(self.putEntryFunction)
        putEntryPage.goBackButton.clicked.connect(lambda: self.goBackButtonFunction(putEntryPage))

        # Get Entry Page Buttons.
        getEntryPage = self.mainWindow.getEntryPage
        getEntryPage.doActionButton.clicked.connect(self.getEntryFunction)
        getEntryPage.goBackButton.clicked.connect(lambda: self.goBackButtonFunction(getEntryPage))

        # Update Entry Page Buttons.
        updateEntryPage = self.mainWindow.updateEntryPage
        updateEntryPage.doActionButton.clicked.connect(self.updateEntryFunction)
        updateEntryPage.goBackButton.clicked.connect(lambda: self.goBackButtonFunction(updateEntryPage))

        # See Entries.
        seeEntriesPage = self.mainWindow.seeEntriesPage
        seeEntriesPage.goBackButton.clicked.connect(lambda: self.goBackButtonFunction(seeEntriesPage))

        # Change Primary Password.
        changePrimaryPasswordPage = self.mainWindow.changePrimaryPasswordPage
        changePrimaryPasswordPage.goBackButton.clicked.connect(lambda: self.goBackButtonFunction(changePrimaryPasswordPage))
        changePrimaryPasswordPage.doActionButton.clicked.connect(self.changePrimaryPasswordFuction)

    def changePrimaryPasswordFuction(self):
        changePrimaryPasswordPage = self.mainWindow.changePrimaryPasswordPage

        oldPassword = changePrimaryPasswordPage.oldPasswordLineEdit.text()
        newPassword = changePrimaryPasswordPage.newPasswordLineEdit.text()
        confirmNewPassword = changePrimaryPasswordPage.confirmNewPasswordLineEdit.text()

        if newPassword == confirmNewPassword:
            if self.working.changePrimaryPassword(oldPassword, newPassword):
                updateQLabel(changePrimaryPasswordPage.statusLine, "Updated")
            else:
                updateQLabel(changePrimaryPasswordPage, "Wrong old password")
        else:
            updateQLabel(changePrimaryPasswordPage.statusLine, "New Password and confirm password do not match.")

    def updateEntryFunction(self):
        updateEntryPage = self.mainWindow.updateEntryPage
        
        oldEmail = updateEntryPage.oldEmailLineEdit.text()
        oldWebsite = updateEntryPage.oldWebsiteLineEdit.text()
        email = updateEntryPage.emailLineEdit.text()
        website = updateEntryPage.websiteLineEdit.text()
        password = updateEntryPage.passwordLineEdit.text()

        self.working.updateEntry(oldEmail, oldWebsite, email, website, password)
        updateQLabel(updateEntryPage.statusLine, "Updated.")
        #updateQLabel(updateEntryPage.statusLine, "Something went wrong.")

    def getEntryFunction(self):
        getEntryPage = self.mainWindow.getEntryPage

        website = getEntryPage.websiteLineEdit.text()
        email = getEntryPage.emailLineEdit.text()

        ans = self.working.getEntry(email, website)
        if ans != "":
            copy(ans)
            updateQLabel(getEntryPage.statusLine, "Copied to clipboard.")
        else:
            updateQLabel(getEntryPage.statusLine, "Wrong entry.")

    def putEntryFunction(self):
        putEntryPage = self.mainWindow.putEntryPage
        
        website = putEntryPage.websiteLineEdit.text()
        email = putEntryPage.emailLineEdit.text()
        password = putEntryPage.passwordLineEdit.text()
        ans = self.working.putEntry(email, website, password) 
        if ans:
            updateQLabel(putEntryPage.statusLine, "Done.")
        else:
            updateQLabel(putEntryPage.statusLine, "Entry already exists.")

    def logoutFunction(self):
        self.mainWindow.loginPage.passwordLineEdit.setText("")
        self.working = None
        updateQLabel(self.mainWindow.loginPage.statusLine, "")
        self.mainWindow.workingPage.hide()
        self.mainWindow.loginPage.show()

    def goToUpdateEntryPageFunction(self):
        updateEntryPage = self.mainWindow.updateEntryPage

        updateEntryPage.oldEmailLineEdit.setText("")
        updateEntryPage.oldWebsiteLineEdit.setText("")
        updateEntryPage.passwordLineEdit.setText("")
        updateEntryPage.emailLineEdit.setText("")
        updateEntryPage.websiteLineEdit.setText("")

        updateQLabel(updateEntryPage.statusLine, "")

        self.mainWindow.workingPage.hide()
        self.mainWindow.updateEntryPage.show()

    def goToSeeEntriesPageFunction(self):
        entries = self.working.seeEntries()

        layout = self.mainWindow.seeEntriesPage.gridLayout

        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().setParent(None)

        emailLabel = qtw.QLabel("Email: ")
        layout.addWidget(emailLabel, 0, 0)
        websiteLabel = qtw.QLabel("Website: ")
        layout.addWidget(websiteLabel, 0, 1)

        count = 1

        for i in entries:
            emailLabel = qtw.QLabel(i[0])
            layout.addWidget(emailLabel, count, 0)
            
            websiteLabel = qtw.QLabel(i[1])
            layout.addWidget(websiteLabel, count, 1)

            button = qtw.QPushButton("Get this entry")
            layout.addWidget(button, count, 2)
            button.clicked.connect(lambda: copy(self.working.getEntry(i[0], i[1])))

            button = qtw.QPushButton("Update this entry")
            layout.addWidget(button, count, 3)
            button.clicked.connect(lambda: self.updateEntryFromSeeEntries(i[0], i[1]))

        self.mainWindow.workingPage.hide()
        self.mainWindow.seeEntriesPage.show()

    def updateEntryFromSeeEntries(self, email, website):
        updateEntryPage = self.mainWindow.updateEntryPage
        updateEntryPage.oldEmailLineEdit.setText(email)
        updateEntryPage.oldWebsiteLineEdit.setText(website)
        updateEntryPage.emailLineEdit.setText("")
        updateEntryPage.websiteLineEdit.setText("")
        updateEntryPage.passwordLineEdit.setText("")

        updateQLabel(updateEntryPage, "")

        self.mainWindow.seeEntriesPage.hide()
        updateEntryPage.show()

    def goToChangePrimaryPasswordPageFunction(self):    
        cppp = self.mainWindow.changePrimaryPasswordPage

        cppp.confirmNewPasswordLineEdit.setText("")
        cppp.newPasswordLineEdit.setText("")
        cppp.oldPasswordLineEdit.setText("")

        updateQLabel(cppp.statusLine, "")

        self.mainWindow.workingPage.hide()
        self.mainWindow.changePrimaryPasswordPage.show()

    def goToPutEntryPageFunction(self):
        pe = self.mainWindow.putEntryPage

        pe.emailLineEdit.setText("")
        pe.websiteLineEdit.setText("")
        pe.passwordLineEdit.setText("")

        updateQLabel(pe.statusLine, "")

        self.mainWindow.workingPage.hide()
        self.mainWindow.putEntryPage.show()

    def goToGetEntryPageFunction(self):
        ge = self.mainWindow.getEntryPage

        ge.emailLineEdit.setText("")
        ge.websiteLineEdit.setText("")

        updateQLabel(ge.statusLine, "")

        self.mainWindow.workingPage.hide()
        self.mainWindow.getEntryPage.show()

    def checkLogin(self):
        self.working = Working(self.mainWindow.loginPage.passwordLineEdit.text())

        if self.working.loginStatus:
            self.mainWindow.loginPage.hide()
            self.mainWindow.workingPage.show() 
        else:
            self.working = None
            updateQLabel(self.mainWindow.loginPage.statusLine, "Wrong Password")

    def goBackButtonFunction(self, fromWidget):
        fromWidget.hide()
        self.mainWindow.workingPage.show()

def main():
    gui = GUI()