#! /usr/bin/env python3
import os

NOT_EXIST_ERR="that file does not exist!"

file=str(input("*.toc file: "))
if os.path.exists(file):
    pathChange=str(input("where is the *.toc.bin file for this *.toc? :"))
    if os.path.exists(pathChange):
        ofile="delta."+file
        tocF=open(ofile,"w")
    
        with open(file,"r") as toc:
            for line in toc:
                keyword=line[:4]
                if keyword == "FILE":
                    line=line.split("\"")
                    line[1]='"'+pathChange+'"'
                    line=''.join(line)
                    tocF.write(line)
                    print(line)
                else:
                    tocF.write(line)
                    print(line)
    else:
        print(NOT_EXIST_ERR)
else:
    print(NOT_EXIST_ERR)
