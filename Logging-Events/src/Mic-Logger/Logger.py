import subprocess
from time import sleep
import logging
from sys import platform

DELAY = 0.5

def startMicLogging(fileName):  
    if platform.lower().startswith('win'):
        #For Windows.
        pass # TODO
    else: # Not implemented for Mac.
        # For Linux.
        global DELAY # The delay between two tries.
        logging.basicConfig(filename=fileName, level=logging.DEBUG, format='%(asctime)s: %(message)s')
    
        while True:
            process = subprocess.Popen(['lsof', '/dev/snd/controlC0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # We get log info from Linux through with subprocess.
            stdout, stderr = process.communicate()
            # We execute the process.
            stdout = [x.split() for x in stdout.decode().split('\n')]   
            # We split the output so work gets easier.            
            for x in stdout:
                if len(x) > 0 and x[0] != 'COMMAND':
                    # We check if the output needs to be logged.
                    logging.info('{}, {}'.format(x[0], x[1]))
        
            sleep(DELAY)