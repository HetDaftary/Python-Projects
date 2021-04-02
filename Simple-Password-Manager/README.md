# Simple-Password-Manager

A python based simple password manager project with sqlite3 and encryption.

Encryption Algorithm used is AES-256
Private Key made using SHA-256
Authentication done using SHA-512

## Features:
* Simple command line based work.
* When getting an entry, it automatically puts the pass in the clipboard so you can paste it in the website.
* Supports multiple rounds of hashing. Currently setup for 1000 rounds of hash function. 
* Easy to change the number of rounds, just need to open Encryption.py and change the HASH_COUNT constant.
## How to run it:
* Step 1: Setup. For this run, the setup.py file and enter the password.
* Step 2: Use: For this, run the command-line.py when you want to use it.
