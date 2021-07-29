# PyQt5 application related.
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from sys import exit
from darkdetect import isDark # This one detects if OS is using dark theme or light theme.
from qt_material import apply_stylesheet # This one is for the themes.
from clipboard import copy # To copy something in clipboard.

# Password manager working related.
from src.working import Working

styleFileName = './src/GUI/css/main.qss'
appSize = 960, 540
appName = 'Simple-Password-Manager'
darkTheme, lightTheme = 'dark_blue.xml', 'light_blue.xml'

def updateQLabel(label, text):
    label.setText(text)
    label.adjustSize()

# Change Primary Password Page UI
class ChangePrimaryPassword(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        vboxLayout = QVBoxLayout()
        self.setLayout(vboxLayout)
        
        detailsWidget = QWidget()
        detailsLayout = QGridLayout()
        detailsWidget.setLayout(detailsLayout)

        enterCurrentPasswordLabel = QLabel('Enter Current Password: ')
        enterCurrentPasswordLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        detailsLayout.addWidget(enterCurrentPasswordLabel, 0, 0)
        self.currentPasswordLineEdit = QLineEdit()
        self.currentPasswordLineEdit.setEchoMode(QLineEdit.Password)
        detailsLayout.addWidget(self.currentPasswordLineEdit, 0, 1)

        enterNewPasswordLabel = QLabel('Enter New Password: ')
        enterNewPasswordLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        detailsLayout.addWidget(enterNewPasswordLabel, 1, 0)
        self.newPasswordLineEdit = QLineEdit()
        self.newPasswordLineEdit.setEchoMode(QLineEdit.Password)
        detailsLayout.addWidget(self.newPasswordLineEdit, 1, 1)

        confirmNewPasswordLabel = QLabel('Confirm New Password: ')
        confirmNewPasswordLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        detailsLayout.addWidget(confirmNewPasswordLabel, 2, 0)
        self.confirmNewPasswordLineEdit = QLineEdit()
        self.confirmNewPasswordLineEdit.setEchoMode(QLineEdit.Password)
        detailsLayout.addWidget(self.confirmNewPasswordLineEdit, 2, 1)

        vboxLayout.addWidget(detailsWidget)

        self.statusLine = QLabel('')
        vboxLayout.addWidget(self.statusLine)

        buttonsWidget = QWidget()
        buttonsLayout = QHBoxLayout()
        buttonsWidget.setLayout(buttonsLayout)
        self.goBackButton = QPushButton('Go Back')
        buttonsLayout.addWidget(self.goBackButton)
        self.changePasswordButton = QPushButton('Change Password')
        buttonsLayout.addWidget(self.changePasswordButton)

        vboxLayout.addWidget(buttonsWidget)

# Update Entry page UI
class UpdateEntry(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        vboxLayout = QVBoxLayout()
        self.setLayout(vboxLayout)

        detailsWidget = QWidget()
        detailsLayout = QGridLayout()
        detailsWidget.setLayout(detailsLayout)

        oldWebsiteLabel = QLabel('Old Website:')
        oldWebsiteLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        detailsLayout.addWidget(oldWebsiteLabel, 0, 0)
        self.oldWebsiteLineEdit = QLineEdit()
        detailsLayout.addWidget(self.oldWebsiteLineEdit, 0, 1)

        oldEmailLabel = QLabel('Old Email:')
        oldEmailLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        detailsLayout.addWidget(oldEmailLabel, 1, 0)
        self.oldEmailLineEdit = QLineEdit()
        detailsLayout.addWidget(self.oldEmailLineEdit, 1, 1)

        newWebsiteLabel = QLabel('New Website:')
        newWebsiteLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter) 
        detailsLayout.addWidget(newWebsiteLabel, 2, 0)
        self.newWebsiteLineEdit = QLineEdit()
        detailsLayout.addWidget(self.newWebsiteLineEdit, 2, 1)

        newEmailLabel = QLabel('New Email:')
        newEmailLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        detailsLayout.addWidget(newEmailLabel, 3, 0)
        self.newEmailLineEdit = QLineEdit()
        detailsLayout.addWidget(self.newEmailLineEdit, 3, 1)

        newPassword = QLabel('New Password: ')
        newPassword.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        detailsLayout.addWidget(newPassword, 4, 0)
        self.newPasswordLineEdit = QLineEdit()
        self.newPasswordLineEdit.setEchoMode(QLineEdit.Password)
        detailsLayout.addWidget(self.newPasswordLineEdit, 4, 1)

        vboxLayout.addWidget(detailsWidget)

        self.statusLabel = QLabel('')
        vboxLayout.addWidget(self.statusLabel)

        buttonsWidget = QWidget()
        buttonsLayout = QHBoxLayout()
        buttonsWidget.setLayout(buttonsLayout)

        self.goBackButton = QPushButton('Go Back')
        buttonsLayout.addWidget(self.goBackButton)

        self.updateEntryButton = QPushButton('Update Entry')
        buttonsLayout.addWidget(self.updateEntryButton)

        vboxLayout.addWidget(buttonsWidget)

# PutEntry Page UI
class PutEntry(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        vboxLayout = QVBoxLayout()
        self.setLayout(vboxLayout)
        
        detailsWidget = QWidget()
        detailsLayout = QGridLayout()
        detailsWidget.setLayout(detailsLayout)

        websiteLabel = QLabel('Website: ')
        detailsLayout.addWidget(websiteLabel, 0, 0)
        self.websiteLine = QLineEdit()
        detailsLayout.addWidget(self.websiteLine, 0, 1)

        emailLabel = QLabel('Email: ')
        detailsLayout.addWidget(emailLabel, 1, 0)
        self.emailLine = QLineEdit()
        detailsLayout.addWidget(self.emailLine, 1, 1)

        passwordLabel = QLabel('Password: ')
        detailsLayout.addWidget(passwordLabel, 2, 0)
        self.passwordLine = QLineEdit()
        self.passwordLine.setEchoMode(QLineEdit.Password)
        detailsLayout.addWidget(self.passwordLine, 2, 1)

        vboxLayout.addWidget(detailsWidget)

        self.statusLine = QLabel('')
        vboxLayout.addWidget(self.statusLine)

        buttonWidget = QWidget()
        hBoxLayout = QHBoxLayout()
        buttonWidget.setLayout(hBoxLayout)

        self.goBackButton = QPushButton('Go Back')
        hBoxLayout.addWidget(self.goBackButton)

        self.putEntryButton = QPushButton('Put Entry')
        hBoxLayout.addWidget(self.putEntryButton)

        vboxLayout.addWidget(buttonWidget)

# See Entries Page UI
class SeeEntries(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        ## not a lot to do here rn.
        ## This field is generated on the button click and not here.

    def initUI(self):
        self.seeEntriesLayout = QVBoxLayout()
        self.setLayout(self.seeEntriesLayout)

# Get Entry page UI
class GetEntry(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        vboxLayout = QVBoxLayout()
        self.setLayout(vboxLayout)
        
        websiteAndEmailWid = QWidget()
        websiteAndEmailLayout = QGridLayout()
        websiteAndEmailWid.setLayout(websiteAndEmailLayout)
        
        websiteLabel = QLabel('Website: ')
        websiteLabel.setAlignment(QtCore.Qt.AlignRight)
        websiteAndEmailLayout.addWidget(websiteLabel, 0, 0)

        self.getWebsiteLineEdit = QLineEdit()
        websiteAndEmailLayout.addWidget(self.getWebsiteLineEdit, 0, 1)

        emailLabel = QLabel('Email: ')
        emailLabel.setAlignment(QtCore.Qt.AlignRight)
        websiteAndEmailLayout.addWidget(emailLabel, 1, 0)

        self.getEmailLineEdit = QLineEdit()
        websiteAndEmailLayout.addWidget(self.getEmailLineEdit, 1, 1)

        vboxLayout.addWidget(websiteAndEmailWid)

        self.statusLabel = QLabel('')
        vboxLayout.addWidget(self.statusLabel)

        buttonsWidget = QWidget()
        buttonsLayout = QHBoxLayout()
        buttonsWidget.setLayout(buttonsLayout)

        self.goBackButton = QPushButton('Go Back')
        buttonsLayout.addWidget(self.goBackButton)
        self.getPasswordButton = QPushButton('Get Password')
        buttonsLayout.addWidget(self.getPasswordButton)

        vboxLayout.addWidget(buttonsWidget)

# UI of login pages.
class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # login page has vboxLayout
        vBox = QVBoxLayout()
        self.setLayout(vBox)
        self.GetPrimaryPasswordWidget = QWidget()
        hBox = QHBoxLayout()
        self.GetPrimaryPasswordWidget.setLayout(hBox)
        askForPasswordLabel = QLabel('Enter Password:')
        hBox.addWidget(askForPasswordLabel)
        self.askForPasswordLineEdit = QLineEdit()
        self.askForPasswordLineEdit.setEchoMode(QLineEdit.Password)
        hBox.addWidget(self.askForPasswordLineEdit)
        vBox.addWidget(self.GetPrimaryPasswordWidget)
        self.statusLabel = QLabel('')
        vBox.addWidget(self.statusLabel)
        self.loginButton = QPushButton('Login')
        vBox.addWidget(self.loginButton)

class WorkingPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        gridLayout = QGridLayout()
        self.setLayout(gridLayout)
        self.goToGetEntryButton = QPushButton('Get Entry')
        self.goToPutEntryButton = QPushButton('Put Entry')
        self.goToUpdateEntryButton = QPushButton('Update Entry')
        self.goToSeeEntriesButton = QPushButton('See Entries')
        self.goToChangePasswordButton = QPushButton('Change Primary Password')
        self.logoutButton = QPushButton('Logout')

        gridLayout.addWidget(self.goToChangePasswordButton, 0, 0)
        gridLayout.addWidget(self.goToGetEntryButton, 0, 1)
        gridLayout.addWidget(self.goToPutEntryButton, 0, 2)
        gridLayout.addWidget(self.goToUpdateEntryButton, 1, 0)
        gridLayout.addWidget(self.goToSeeEntriesButton, 1, 1)
        gridLayout.addWidget(self.logoutButton, 1, 2)

# UI of main Window.
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Resizing main window to appSize(960x540).
        self.resize(*appSize)
        self.mainWin = QWidget()
        self.hBoxLayout = QHBoxLayout()
        self.mainWin.setLayout(self.hBoxLayout)

        self.initPages()
        # Gets every page and hides them all except login page
        self.initMenuBar()
        # To get 

        self.setCentralWidget(self.mainWin)
        self.show()

    def initPages(self):
        self.loginPage = LoginPage()
        self.getEntryPage = GetEntry()
        self.putEntryPage = PutEntry()
        self.updateEntryPage = UpdateEntry()
        self.seeEntriesPage = SeeEntries()
        self.changePrimaryPasswordPage = ChangePrimaryPassword()
        self.workingPage = WorkingPage()

        # Adding pages to mainWin.
        self.hBoxLayout.addWidget(self.loginPage)
        self.hBoxLayout.addWidget(self.getEntryPage)
        self.hBoxLayout.addWidget(self.putEntryPage)
        self.hBoxLayout.addWidget(self.updateEntryPage)
        self.hBoxLayout.addWidget(self.seeEntriesPage)
        self.hBoxLayout.addWidget(self.changePrimaryPasswordPage)
        self.hBoxLayout.addWidget(self.workingPage)

        self.workingPage.hide()
        self.changePrimaryPasswordPage.hide()
        self.seeEntriesPage.hide()
        self.updateEntryPage.hide()
        self.putEntryPage.hide()
        self.getEntryPage.hide()

    def initMenuBar(self):
        self.menuBar = QMenuBar()
        self.setMenuBar(self.menuBar)

        self.themeMenu = QMenu('Theme options')

        self.osPreferredTheme = QAction('OS Preferred Theme')
        self.themeMenu.addAction(self.osPreferredTheme)
        self.darkTheme = QAction('Dark Theme')
        self.themeMenu.addAction(self.darkTheme)
        self.lightTheme = QAction('Light Theme')
        self.themeMenu.addAction(self.lightTheme)

        self.menuBar.addMenu(self.themeMenu)

# This class mainly deals with actions to be taken.
# All the buttons will get action here.
class GUIClass(QApplication):
    def __init__(self):
        super().__init__([appName])
        self.mainWindow = MyMainWindow()

        self.initWorking()

        self.initStyle()
        # Giving style to our app.

        self.initButtonActions()
        # Giving actions to the buttons.

        self.initMenuBarActions()

        exit(self.exec_())
        # Closing Python completely once the app's closed.

    def initWorking(self):
        self.working = None

    # Sets in initial style.
    def initStyle(self):
        global darkTheme, lightTheme
        if isDark():
            apply_stylesheet(self, darkTheme)
        else:
            apply_stylesheet(self, lightTheme)

    # Gives actions to the buttons
    # initMenuBarActions() after the functions of button actions.
    def initButtonActions(self):
        # Login Page buttons
        self.mainWindow.loginPage.loginButton.clicked.connect(self.checkLogin)
        
        # Working Page buttons
        self.mainWindow.workingPage.goToGetEntryButton.clicked.connect(self.goToGetEntryFunction)
        self.mainWindow.workingPage.goToPutEntryButton.clicked.connect(self.goToPutEntryFunction)
        self.mainWindow.workingPage.goToUpdateEntryButton.clicked.connect(self.goToUpdateEntryFunction)
        self.mainWindow.workingPage.goToSeeEntriesButton.clicked.connect(lambda: self.goToSeeEntriesFunction())
        self.mainWindow.workingPage.goToChangePasswordButton.clicked.connect(self.goToChangePasswordButton)
        self.mainWindow.workingPage.logoutButton.clicked.connect(self.logoutFunction)

        # PutEntry Page buttons
        self.mainWindow.putEntryPage.putEntryButton.clicked.connect(self.putEntryFunction)
        self.mainWindow.putEntryPage.goBackButton.clicked.connect(lambda: self.goBackFunction(self.mainWindow.putEntryPage))

        # GetEntry Page buttons
        self.mainWindow.getEntryPage.getPasswordButton.clicked.connect(self.getPasswordFunction)
        self.mainWindow.getEntryPage.goBackButton.clicked.connect(lambda: self.goBackFunction(self.mainWindow.getEntryPage))

        # UpdateEntry Page buttons
        self.mainWindow.updateEntryPage.updateEntryButton.clicked.connect(self.updateEntryFunction)
        self.mainWindow.updateEntryPage.goBackButton.clicked.connect(lambda: self.goBackFunction(self.mainWindow.updateEntryPage))

        # ChangePassword Page buttons
        self.mainWindow.changePrimaryPasswordPage.changePasswordButton.clicked.connect(self.changePrimaryPasswordFunction)
        self.mainWindow.changePrimaryPasswordPage.goBackButton.clicked.connect(lambda: self.goBackFunction(self.mainWindow.changePrimaryPasswordPage))

    ## Functions to give actions to the buttons. Start.
    def checkLogin(self):
        self.working = Working(self.mainWindow.loginPage.askForPasswordLineEdit.text())

        if self.working.didPassWork():
            self.mainWindow.loginPage.hide()
            self.mainWindow.workingPage.show()
        else:
            updateQLabel(self.mainWindow.loginPage.statusLabel, 'Wrong Password')
            self.working = None
    
    def goToGetEntryFunction(self):
        self.mainWindow.getEntryPage.getWebsiteLineEdit.setText('')
        self.mainWindow.getEntryPage.getEmailLineEdit.setText('')
        updateQLabel(self.mainWindow.getEntryPage.statusLabel, '')

        self.mainWindow.workingPage.hide()
        self.mainWindow.getEntryPage.show()

    def goToChangePasswordButton(self):
        self.mainWindow.changePrimaryPasswordPage.currentPasswordLineEdit.setText('')
        self.mainWindow.changePrimaryPasswordPage.newPasswordLineEdit.setText('')
        self.mainWindow.changePrimaryPasswordPage.confirmNewPasswordLineEdit.setText('')
        updateQLabel(self.mainWindow.changePrimaryPasswordPage.statusLine, '')

        self.mainWindow.workingPage.hide()
        self.mainWindow.changePrimaryPasswordPage.show()

    def goToPutEntryFunction(self):
        self.mainWindow.putEntryPage.websiteLine.setText('')
        self.mainWindow.putEntryPage.emailLine.setText('')
        self.mainWindow.putEntryPage.passwordLine.setText('')
        updateQLabel(self.mainWindow.putEntryPage.statusLine, '')

        self.mainWindow.workingPage.hide()
        self.mainWindow.putEntryPage.show()

    def goToUpdateEntryFunction(self):
        self.mainWindow.updateEntryPage.oldWebsiteLineEdit.setText('')
        self.mainWindow.updateEntryPage.oldWebsiteLineEdit.setText('')
        self.mainWindow.updateEntryPage.newWebsiteLineEdit.setText('')
        self.mainWindow.updateEntryPage.newWebsiteLineEdit.setText('')
        self.mainWindow.updateEntryPage.newPasswordLineEdit.setText('')
        updateQLabel(self.mainWindow.updateEntryPage.statusLabel, '')

        self.mainWindow.workingPage.hide()
        self.mainWindow.updateEntryPage.show()

    def cleanAWidget(self, layoutToClean):
        for i in reversed(range(layoutToClean.count())):
            layoutToClean.itemAt(i).widget().setParent(None)

    def goToSeeEntriesFunction(self):
        self.currentEntries = self.working.seeEntries()
        self.cleanAWidget(self.mainWindow.seeEntriesPage.seeEntriesLayout)
        self.detailsWidget = QWidget()
        self.detailsLayout = QGridLayout()
        self.detailsWidget.setLayout(self.detailsLayout)

        self.emailLabel = QLabel('Email')
        self.emailLabel.setAlignment(QtCore.Qt.AlignTop)
        self.detailsLayout.addWidget(self.emailLabel, 0, 0)
        self.websiteLabel = QLabel('Website')
        self.websiteLabel.setAlignment(QtCore.Qt.AlignTop)
        self.detailsLayout.addWidget(self.websiteLabel, 0, 1)
            
        count = 1
        for i in range(len(self.currentEntries)):
            self.detailsLayout.addWidget(QLabel(text=self.currentEntries[i][0]), count, 0)
            self.detailsLayout.addWidget(QLabel(text=self.currentEntries[i][1]), count, 1)
            
            currentButton = QPushButton("Get this Entry")
            currentButton.clicked.connect(lambda _, a=i: self.getPasswordFromButton(self.currentEntries[a]))
            self.detailsLayout.addWidget(currentButton, count, 2)

            currentUpdateButton = QPushButton("Update this Entry")
            currentUpdateButton.clicked.connect(lambda _, a=i: self.updateEntryFromSeeEntries(self.currentEntries[a]))
            self.detailsLayout.addWidget(currentUpdateButton, count, 3)
            
            count += 1

        self.mainWindow.seeEntriesPage.seeEntriesLayout.addWidget(self.detailsWidget)

        self.goBackButton = QPushButton("Go Back")
        self.goBackButton.clicked.connect(lambda: self.goBackFunction(self.mainWindow.seeEntriesPage))
        self.mainWindow.seeEntriesPage.seeEntriesLayout.addWidget(self.goBackButton)

        self.mainWindow.workingPage.hide()
        self.mainWindow.seeEntriesPage.show()

    def getPasswordFromButton(self, entry):
        self.getPassword(toGet[1], toGet[0])

    def getPassword(self, website, email):
        copy(self.working.getEntry(email, website))

    def updateEntryFromSeeEntries(self, entry):
        self.mainWindow.updateEntryPage.oldWebsiteLineEdit.setText(entry[0])
        self.mainWindow.updateEntryPage.oldWebsiteLineEdit.setText(entry[1])
        self.mainWindow.updateEntryPage.newWebsiteLineEdit.setText('')
        self.mainWindow.updateEntryPage.newWebsiteLineEdit.setText('')
        self.mainWindow.updateEntryPage.newPasswordLineEdit.setText('')
        updateQLabel(self.mainWindow.updateEntryPage.statusLabel, '')
    
    def logoutFunction(self):
        # Removing details and stuff of previous session.
        self.working = None
        self.mainWindow.loginPage.askForPasswordLineEdit.setText('')

        self.mainWindow.workingPage.hide()
        self.mainWindow.loginPage.show()

    def goBackFunction(self, fromGoBack):
        # This goBackFunction is called for every go back button.
        fromGoBack.hide()
        self.mainWindow.workingPage.show()
    
    def getPasswordFunction(self):
        try:    
            details = [
                self.mainWindow.getEntryPage.getEmailLineEdit.text(),
                self.mainWindow.getEntryPage.getWebsiteLineEdit.text()
            ]
            copy(self.working.getPassword(*details))
            updateQLabel(self.mainWindow.getEntryPage.statusLabel, 'Copied to clipboard')
        except Exception:
            updateQLabel(self.mainWindow.getEntryPage.statusLabel, 'Entry does not exists')
    
    def putEntryFunction(self):
        try:
            details = [
                self.mainWindow.putEntryPage.emailLine.text(), 
                self.mainWindow.putEntryPage.websiteLine.text(), 
                self.mainWindow.putEntryPage.passwordLine.text()
            ]
            self.working.putEntry(*details)
            updateQLabel(self.mainWindow.putEntryPage.statusLine, 'Entry added')
        except:
            updateQLabel(self.mainWindow.putEntryPage.statusLine, 'Error: Entry already exists')
    
    def updateEntryFunction(self):
        try:
            # I added the list of params here because will never be clear if I directly pass here the values
            details = [
                self.mainWindow.updateEntryPage.oldEmailLineEdit.text(),
                self.mainWindow.updateEntryPage.oldWebsiteLineEdit.text(),
                self.mainWindow.updateEntryPage.newEmailLineEdit.text(),
                self.mainWindow.updateEntryPage.newWebsiteLineEdit.text(),
                self.mainWindow.updateEntryPage.newPasswordLineEdit.text()
            ]
            self.working.updateEntry(*details)
            updateQLabel(self.mainWindow.updateEntryPage.statusLabel, 'Entry Updated')
        except Exception:
            updateQLabel(self.mainWindow.updateEntryPage.statusLabel, 'Error')
    
    def changePrimaryPasswordFunction(self):
        details = [
            self.mainWindow.changePrimaryPasswordPage.oldPasswordLineEdit.text(),
            self.mainWindow.changePrimaryPasswordPage.newPasswordLineEdit.text(),
            self.mainWindow.changePrimaryPasswordPage.confirmNewPasswordLineEdit.text()
        ]

        if details[1] != details[2]:
            updateQLabel(self.mainWindow.changePrimaryPasswordPage.statusLine, 'New password does not match')
        else:
            ans = self.working.changePrimaryPassword(details[0], details[1])
            if ans:
                updateQLabel(self.mainWindow.changePrimaryPasswordPage.statusLine, 'Password changed')
            else:
                updateQLabel(self.mainWindow.changePrimaryPasswordPage.statusLine, 'Old password not correct')
    ## Functions to give actions to the buttons. End.

    # Giving actions to menus.
    def initMenuBarActions(self):
        self.mainWindow.osPreferredTheme.triggered.connect(lambda: apply_stylesheet(self, darkTheme if isDark() else lightTheme))
        self.mainWindow.darkTheme.triggered.connect(lambda: apply_stylesheet(self, darkTheme))
        self.mainWindow.lightTheme.triggered.connect(lambda: apply_stylesheet(self, lightTheme))
