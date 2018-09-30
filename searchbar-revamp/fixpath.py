import os,shutil


undes="'[]{}()\""
for root,dirs,fnames in os.walk("resources",topdown=True):
    rootacc=''
    for char in root:
        if char not in undes:
            rootacc+=char
        else:
            rootacc+="_"+str(ord(char))
    if os.path.exists(root):
        print(root,rootacc)
        shutil.move(root,rootacc)


