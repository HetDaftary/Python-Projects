from ..Functions import Functions
import os
# Importing modules.

# Defining constants.
imageExtensions = set(['jpg', 'jpeg', 'png', 'tiff', 'gif', 'bmp'])
# 

# Trying to manage screenshots of my smartphone for this example.
from_ext, to_ext = "png", "jpg" # Need to convert the png images to jpg images to save space.
x, y = 0, 120 # Need to remove useless parts by cropping. x, y mark the starting point.
to_crop_at = (2280, 1080, 3) 
w, h = 1080, 1920 # The size of the final image.


def getNameAndExt(item):
    ans = -1
    for i in range(len(fileName) - 1, -1, -1):
        if item[i] == '.':
            ans = i
            break
    
    if ans > -1:
        if item[-1] != '.':    
            return item[:i], item[i + 1:]
        else:
            return item[:len(item) - 1], ''
    else:
        return item, ''
    return '', ''

def tp(path):

    global imageExtensions, from_ext, to_ext, x, y, to_crop_at, w, h

    lsOut = os.listdir(path)

    for item in lsOut:
        cur = os.path.join(path, item)
        # Current Path. 
        if os.path.isdir(cur):
            tp(cur)
        else:
            fileName, ext = getNameAndExt(item)
            if ext in imageExtensions:
                img = Functions.readImage(cur)
                
                # TODO the task of editing the images here.
                if img.shape == to_crop_at:
                    img = Functions.crop(img, x, y, w, h)
                if ext == from_ext:
                    writeImage(img, path + fileName + to_ext)

if __name__ == "__main__":
    tp("Path goes here.")