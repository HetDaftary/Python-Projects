import os 
from typing import *

FILENAME = "mylist.txt"

'''
@breif Dependency for merge video Functions. Creates the file which stores the video names.
This will be a temporary file which will be deleted after the merge is done.
@param videoNames: to make the videos file
'''
def makeFile(videoNames: List[str]):
    global FILENAME

    with open(FILENAME, "w") as f:
        for name in videoNames:
            f.write("file '{}'\n".format(name))

'''
@breif A function to merge same type of videos.
@param videoNames: list of video names
@param outputName: output name
@return None
'''
def mergeVideosSameProfile(videoNames: List[str], outputName: str) -> None:
    global FILENAME
    
    makeFile(videoNames)    
    os.system("ffmpeg -f concat -safe 0 -i {} -c copy {}".format(FILENAME, outputName))
    os.remove(FILENAME)

'''
@breif Merge videos with rendering to a particular resolution and framerate.
@param videoNames: list of video names
@param outputName: output name
@param fps: fps
@param quality: width, height tuple.
@return: None
'''
def mergeVideosDifferentProfile(videoNames: List[str], outputName: str, quality: Tuple[int], fps: int) -> None:
    global FILENAME

    makeFile(videoNames)

    os.system("ffmpeg -f concat -i {} -vf scale={} -framerate {} {}".format(FILENAME, ':'.join([str(x) for x in quality]), fps, outputName))
    os.remove(FILENAME)