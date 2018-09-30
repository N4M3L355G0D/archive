import os,shutil
undes="'[]{}()\""
for root,dirs,fnames in os.walk("resources",topdown=True):
    for fname in fnames:
        path=os.path.join(root,fname)
        acc=''
        for char in path:
            if char not in undes:
                acc+=char
            else:
                acc+="_"+str(ord(char))
        if os.path.exists(path):
            shutil.move(path,acc)

