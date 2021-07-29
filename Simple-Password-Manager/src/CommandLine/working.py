from os import system
from time import sleep
from clipboard import copy
from sys import platform
from src.working import Working
from getpass import getpass

# someConstants.
padVal = 30
clear = None
if platform == "win32" or platform == "win64":
    clear = "cls" # This constant will be used as a command which depends on the os.
else:
    clear = "clear"

def printWithPad(item):
    temp = item[0]
    if len(temp) < padVal:
        temp += " "*(padVal - len(temp))
    temp += ":"
    print(temp, item[1])

# For the decoration of see Entries.
def toPrint(ls):
    global padVal
    for item in ls:
        printWithPad(item)

    # Our working object.
    working = None

def main():
    while True:
        print("Enter q if you want to quit.")
        i = getpass(prompt="Enter the password: ")

        working = Working(i)
        if working.didPassWork():
            print("Session Granted.")
            sleep(1)
            break
        if i == 'q' or i == 'Q':
            exit(0) # Exiting as session not granted.

    system(clear)
    # Clearing the output screen.

    while True:
        print("*"*padVal)
        print("Enter the query. ")
        print("q for quit.\ns for see entries.\ng to get an query.\np for putting an entry.\nu to update an entry.\nc to clear the terminal.\nch for changing the password.")
        print("*"*padVal, end = "\n\n")

        inVal = input("Enter the option: ").lower()

        if inVal == 'q':
            exit(0)
        elif inVal == 's':
            toPrint(working.seeEntries())
        elif inVal == 'c':
            system(clear)
        elif inVal == 'p':
            email = input("Enter the email: ")
            website = input("Enter the website: ")
            password = input("Enter the passwords: ")
            working.putEntry(email, website, password)
        elif inVal == 'g':
            try:
                email = input("Enter the email: ")
                website = input("Enter the website: ")
                copy(working.getEntry(email, website))
                print("Password copied to clipboard.")
            except:
                print("Entry does not exists")
        elif inVal == 'ch':
                oldPassword = input('Enter old password').rstrip()
                newPassword = input('Enter new password').rstrip()
                newPasswordAgain = input('Confirm new password').rstrip()
                if newPassword == newPasswordAgain:
                    didChange = working.changeMasterPassword(oldPassword, newPassword)
                    if didChange:
                        print('Wrong password. Not successful.')
                    else:
                        print('Successful. Password changed.')
                else:
                    print('confirmation failed.')
        elif inVal == 'u':
                oldEmail = input("Enter the old email")
                oldWebsite = input("Enter the old website")
                email = input("Enter the new email: ")
                website = input("Enter the new website: ")
                password = input("Enter the new passwords: ")
                working.updateEntry(oldEmail, oldWebsite, email, website, password)
        else:
            print("This option is not available.")