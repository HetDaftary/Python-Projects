from src.working.working import Working
from sys import platform
import os
from clipboard import copy
from getpass import getpass

def pad(s: str) -> str:
    if len(s) < 50:
        s += " " * (50 - len(s))
    return s

def main():
    primaryPassword = None 
    
    while True:
        print("Enter q if you want to quit.")
        primaryPassword = getpass("Enter the primary password: ").strip()
        if primaryPassword == "q":
            break
        working = Working(primaryPassword)
        if working.loginStatus:
            break
            # Login successful.
        else:
            continue
            # Login not successful.
    
    if primaryPassword == 'q':
        exit(0)

    while True:
        print("*"*50)
        print("Enter q if you want to quit.")
        print("Enter ch to change primary password.")
        print("Enter s to see entries.")
        print("Enter c to clear terminal.")
        print("Enter p to put Entry.")
        print("Enter g to get Entry.")
        print("Enter u to update entry.")
        print("*"*50, '\n\n')

        command = input("Enter command: ").strip()

        if command == 'q':
            break
        elif command == 'ch':
            oldPassword = getpass("Enter old password: ").strip()
            newPassword = getpass("Enter new password: ").strip()
            confirmPassword = getpass("Enter new password again: ").strip()

            if newPassword == confirmPassword:
                if working.changePrimaryPassword(oldPassword, newPassword):
                    print("Password changed successfully.")
                else:
                    print("Old password not correct.")
            else:
                print("Passwords do not match.")
        elif command == 's':
            entries = working.seeEntries()
            for entry in entries:
                print(pad(entry[0]), ":", entry[1])
        elif command == 'c':
            if platform.lower().startswith('win'):
                os.system("cls")
            else:
                os.system("clear")
        elif command == 'p':
            email = input("Enter email: ").strip()
            website = input("Enter website: ").strip()
            password = getpass("Enter password: ").strip()

            if working.putEntry(email, website, password):
                print("Entry added successfully.")
            else:
                print("Entry not added.")
        elif command == 'g':
            email = input("Enter email: ").strip()
            website = input("Enter website: ").strip()
            ans = working.getEntry(email, website)
            if ans != "":
                copy(ans)
            else:
                print("Entry not found.")
        elif command == 'u':
            oldEmail = input("Enter old email: ").strip()
            oldWebsite = input("Enter old website: ").strip()
            newEmail = input("Enter new email: ").strip()
            newWebsite = input("Enter new website: ").strip()
            newPassword = getpass("Enter new password: ").strip()

            working.updateEntry(oldEmail, oldWebsite, newEmail, newWebsite, newPassword)
            print("Entry updated successfully.")
        else:
            print("Invalid command.")
