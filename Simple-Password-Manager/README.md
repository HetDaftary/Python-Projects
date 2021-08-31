# Simple-Password-Manager

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
