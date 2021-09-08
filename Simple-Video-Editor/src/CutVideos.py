from os import system
from typing import * 

'''
@param inputVideoName: Name of input video file.
@param outputVideoName: Name of output video file.
@param start: Start time in string format h:mm:ss
@param end: End time in string format h:mm:ss.
'''
def cutVideo(inputVideoName: str, start: str, end: str, outputVideoName: str) -> None:
    system("ffmpeg -i {} -ss {} -to {} -c copy {}".format(inputVideoName, start, end, outputVideoName))