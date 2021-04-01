import os

def tp(val, path):
    ls = os.listdir(path)

    for i in ls:
        cur = os.path.join(path, i)

        print("--"*val, i)
        if os.path.isdir(cur):
            tp(val + 1, cur)

def DirectoryTree(path):
    print(path.split('/')[-1])
    tp(1, path)

DirectoryTree(os.getcwd())