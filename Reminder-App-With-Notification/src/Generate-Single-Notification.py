from MakeReminder import makeReminder

if __name__ == "__main__":
    timeToNotify = input("Enter time in YYYY-MM-DD HH:MM format: ")
    title = input("Enter title for the notification: ")
    message = input("Enter message for notification: ")
    
    makeReminder(timeToNotify = timeToNotify, title = title, message = message)