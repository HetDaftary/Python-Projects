import sqlite3
from os.path import exists, join, isdir
from .Encryption import hash
from sys import platform
from os import environ, system

createTableSyntax = [
    "CREATE TABLE Passwords (email TEXT, website TEXT, password TEXT, PRIMARY KEY(email,website));",
    "CREATE TABLE PrimaryPassword (primaryPassword TEXT, PRIMARY KEY(primaryPassword));"
]

fileName = None
if platform.lower().startswith("win"):
    fileName = "data\\2.db"
else:
    path = environ["HOME"] + '/.SimplePasswordManager'
    if not isdir(path):
        system(f"mkdir -p {path}")
    fileName = path + '/2.db'

def setup(primaryPassword):
    if exists(fileName):
        raise Exception("File already exists. Delete 2.db if something is wrong")

    conn = sqlite3.connect(fileName)
    cur = conn.cursor()

    for tableSyntax in createTableSyntax:
        cur.execute(tableSyntax)
        conn.commit()

    cur.execute("INSERT INTO PrimaryPassword(primaryPassword) VALUES (\"%s\");" % (hash(primaryPassword)))
    conn.commit()
    cur.close()
    conn.close()

