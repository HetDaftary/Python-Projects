# Simple-Password-Manager

<<<<<<< HEAD
An easy to use password manager made with SQLite and uses SHA-512 based login and AES-256 based encryption.

## TODO

- [x] Make the Backend
    - [x] Make the Encryption module which deals with Encryption and hashing.
    - [x] Make the Working module which deals with SQLite based queries.
- [x] Make the Command-line based frontend
    - [x] Make the Bare minimum frontend.
    - [x] Use getpass to scan passwords.
- [x] PyQt5 GUI front in version 2
    - [x] Make GUI working
        - [x] Make a working GUI:
        - [x] Do the bug fixes
        - [x] Add theme menu: Light theme and dark theme options
        - [x] Do the bug fixes
        - [x] Add system preferred theme
        - [x] Do the bug fixes
    - [x] Make GUI setup
- [ ] PostgreSQL in version 3

## Run 

- For Windows

        .\main.bat

- For Linux

        ./main.sh

## Notes 

- If database exists, then run working.
- Else create database and store primary passwords.
=======
A python based simple password manager project with sqlite3 and encryption.

Encryption Algorithm used is AES-256<br/>
Private Key made using SHA-256<br/>
Authentication done using SHA-512<br/>

## Features:
* Simple command line based work and GUI based operations.
* When getting an entry, it automatically puts the pass in the clipboard so you can paste it in the website.
* Supports multiple rounds of hashing. Currently setup for 1000 rounds of hash function. 
* Easy to change the number of rounds, just need to open Encryption.py and change the HASH_COUNT constant.
* Current Version: <b>1.6</b>
## How to run it:
* Command-Line:
  * Run src/mainCommandline.py and it will launch the required file for command line.
* GUI:
  * Run src/main.py and it will launch the setup if needed or launch the working if setup is done.

<br/>

    python3 -m src.main # To run GUI.
    python3 -m src.mainCommandline # To run CommandLine.


## Images:
<br/>
<img src = "https://github.com/HetDaftary/Python-Projects/blob/master/Simple-Password-Manager/img/1.png">
<br/><br/>
<img src = "https://github.com/HetDaftary/Python-Projects/blob/master/Simple-Password-Manager/img/2.png">
<br/><br/>
<img src = "https://github.com/HetDaftary/Python-Projects/blob/master/Simple-Password-Manager/img/3.png">
<br/><br/>
<img src = "https://github.com/HetDaftary/Python-Projects/blob/master/Simple-Password-Manager/img/4.png">
<br/><br/>
<img src = "https://github.com/HetDaftary/Python-Projects/blob/master/Simple-Password-Manager/img/5.png">
<br/><br/>
<img src = "https://github.com/HetDaftary/Python-Projects/blob/master/Simple-Password-Manager/img/6.png">
>>>>>>> 5232ce7a32d832700ea1db72217dd29a3fcbdf0a
