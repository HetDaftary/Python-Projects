from plyer import notification
from time import sleep
from datetime import datetime
from sys import argv

sleepTime, timeout = 1, 10

def roundDateTime(obj):
    obj = obj.replace(second = 0, microsecond = 0)
    return obj

def makeReminder(timeToNotify, title, message, app_icon = None, toast = False):
    global sleepTime, timeout
    timeToNotify = roundDateTime(datetime.strptime(timeToNotify, '%Y-%m-%d %H:%M'))
    
    # We wait till the time comes.
    while roundDateTime(datetime.now()) != timeToNotify:
        sleep(sleepTime)
   
    # We generate the notification.
    notification.notify(title = title, message = message, timeout = timeout)

if __name__ == "__main__":
    makeReminder(timeToNotify = argv[1],title = argv[2], message = argv[3])