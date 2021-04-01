import os

originalPath = None

def tp(path):
    global originalPath

    ls = os.listdir(path)

    for i in ls:
        cur = os.path.join(path, i)
        if os.path.isdir(cur):
            tp(cur)
        else:
            ext = i.split(".")[-1] # We get the extension of the file.
            toPut = os.path.join(originalPath, ext)
            try:
                os.rename(cur, os.path.join(toPut, i))
            except:
                if not os.path.isfile(cur):
                    os.mkdir(toPut)
                    os.rename(cur, os.path.join(toPut, i))

def tpUtil(op):
    global originalPath
    originalPath = op
    tp(originalPath)

if __name__ == "__main__":
    tpUtil("Path")