import sqlite3
from .Encryption import *
from sys import platform
from os.path import isdir, environ
from os import system 

fileName = None
if platform.lower().startswith("win"):
    fileName = "data\\2.db"
else:
    path = environ["HOME"] + '/.SimplePasswordManager'
    if not isdir(path):
        system(f"mkdir -p {path}")
    fileName = path + '/2.db'

class Working:
    def __init__(self, primaryPass):
        global fileName

        hashOfPass = hash(primaryPass)
        self.conn = sqlite3.connect(fileName)
        self.cur = self.conn.cursor()

        if hashOfPass == self.getPrimaryPass():
            # print("Session Granted")
            self._primaryPass = hashEnc(primaryPass)
        else:
            pass

    def didPassWork(self):
        try:
            return self._primaryPass != None
        except:
            return False

    def getPrimaryPass(self):
        self.cur.execute("SELECT * FROM primaryPassword")
        ans = self.cur.fetchall()[0][0]
        return ans

    def getEntry(self, email, website):
        self.cur.execute(
            "SELECT password FROM Passwords WHERE Passwords.email = \"%s\" AND Passwords.website = \"%s\"" % (
            email, website))
        data = decrypt(self.cur.fetchall()[0][0], self._primaryPass)
        return data

    def putEntry(self, email, website, password):
        enc = encrypt(password, self._primaryPass)
        self.cur.execute(
            "INSERT INTO Passwords(email, website, password) VALUES (\"%s\", \"%s\", \"%s\")" % (email, website, enc))
        self.conn.commit()

    def updateEntry(self, email, website, newEmail, newWebsite, newPassword):
        self.cur.execute(
            "UPDATE Passwords SET email = \"%s\", website = \"%s\", password = \"%s\" WHERE Passwords.email = \"%s\" AND Passwords.website = \"%s\"" % (
            newEmail, newWebsite, encrypt(newPassword, self._primaryPass), email, website))
        self.conn.commit()

    def seeEntries(self):
        self.cur.execute("SELECT email, website FROM Passwords")
        return self.cur.fetchall()

    def changeMasterPassword(self, oldPassword, newPassword):
        oldHash = hash(oldPassword)
        if oldHash != self.getPrimaryPass():
            # Authentication not successful.
            return False
        else:
            # Authentication successful.
            self.cur.execute("SELECT * FROM Passwords")
            data = [list(x) for x in self.cur.fetchall()]

            tempHash = hashEnc(newPassword)

            for i in range(len(data)):
                data[i][2] = encrypt(decrypt(data[i][2], self._primaryPass), tempHash)
            self._primaryPass = tempHash

            for i in data:
                self.cur.execute(
                    "UPDATE Passwords SET password = \"%s\" WHERE Passwords.email = \"%s\" AND Passwords.website = \"%s\"" % (
                    i[2], i[0], i[1]))
            self.cur.execute(
                "UPDATE PrimaryPassword SET primaryPassword = \"%s\" WHERE PrimaryPassword.primaryPassword = \"%s\"" % (
                hash(newPassword), oldHash))
            self.conn.commit()

            return True

    def __del__(self):
        # print("Closing the object")
        self.cur.close()
        self.conn.close()
