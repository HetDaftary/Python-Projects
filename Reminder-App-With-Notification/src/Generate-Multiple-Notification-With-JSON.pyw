#!/usr/bin/env python3

# from MakeReminder import makeReminder
import datetime
from json import loads # To read an excel file.
import subprocess

# To run this files make a csv file with datetime, title and message for notifications. 
# The format for datetime is yyyy-mm-dd hh:mm. It rounds after minutes.

if __name__ == '__main__':
    try:
        # ../data/1.csv for sample file
        filename = input("Enter filename: ")
        
        with open(filename) as fptr:
            # The expected CSV input is in the form of Date and Time.
            
            jsonOutput = loads(fptr.read())
            data = [[x["timeToNotify"], x["title"], x["message"]] for x in jsonOutput]
            
            # Check if you are using a different delimiter
            for row in data:
                subprocess.run(['python3', 'MakeReminder.py'] + row)
                              
    except FileNotFoundError:
        print("Enter valid file name")