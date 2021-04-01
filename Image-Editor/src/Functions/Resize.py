from cv2 import resize as re
from cv2 import INTER_CUBIC

def resize(img, newSize):
    return re(img, newSize, INTER_CUBIC)