import os 

FILENAME = "mylist.txt"

def mergeVideosSameProfile(videoNames, outputName):
    global FILENAME
    
    with open(FILENAME, "w") as f:    
        for name in videoNames:
            f.write("file '{}'\n".format(name))
    
    os.system("ffmpeg -f concat -safe 0 -i {} -c copy {}".format(FILENAME, outputName))
    os.remove(FILENAME)

def mergeVideosDifferentProfile(vidoeNames, outputName, quality):
    pass 
    