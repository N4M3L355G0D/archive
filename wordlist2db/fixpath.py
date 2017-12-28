#1 /usr/bin/python3

import os
for dir,j,fname in os.walk("wlwa"):
    if " " in dir:
            origPath=dir
            newPath=dir.replace(" ","_")
            os.rename(origPath,newPath)
            #print(origPath,newPath)
    for i in fname:
        if " " in i:
            origPath=os.path.join(dir,i)
            newPath=os.path.join(dir,i.replace(" ","_"))
            os.rename(origPath,newPath)
            print(origPath,newPath,sep=" => ")
        
