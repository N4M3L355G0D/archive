#! /usr/bin/python3

#this prog displays output using b'' as sometimes in my current filesystem, i will find
#filenames in binary, which print get thrown for a loop, so using the bytes format skips over that
#if the format is really import, use python3 find.py | sed s/^'b'//g

import os
from re import escape
import subprocess
import math


#set some basic units
kb=math.pow(1024,1)
mb=math.pow(1024,2)
gb=math.pow(1024,3)
tb=math.pow(1024,5)

#set val to whatever file size min 
val=2
#set sizefmt to KB if you want size out to display in kb
sizefmt="GB"
sizefmtd={"KB":kb,"MB":mb,"GB":gb,"TB":tb}
desired_size=val*sizefmtd[sizefmt]

#begin exclude run so values from psuedo filesystems do not pollute output
ignore=set([b'/dev',b'/proc'])
rooted=os.listdir(b"/")
rooted2=list()
for i in rooted:
    pth=b"/"+i
    if not os.path.isfile(pth):
        rooted2.append(pth)

#begin detect and display
for lookie in rooted2:
    if lookie not in ignore:
        for root,dirs,files in os.walk(lookie,topdown=True):
            dirs[:]=[d for d in dirs if d not in ignore]
            for file in files:
                path_escaped=os.path.join(escape(root),escape(file))
                path_not_escape=os.path.join(root,file)
                if os.path.exists(path_not_escape):
                    size=os.path.getsize(path_not_escape)
                    Desired_size=size/sizefmtd[sizefmt]
                    # display size in 2 decimal output
                    desired_size_string='{:.2f}'.format(Desired_size)+" "+sizefmt
                    if size >= desired_size:
                        try:
                            print(desired_size_string,path_not_escape.decode(),sep=" -> ")
                        except:
                            print(desired_size_string,path_not_escape,sep=" -> ")
