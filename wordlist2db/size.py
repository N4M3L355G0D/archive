#! /usr/bin/python3

import sys, os

for line in sys.stdin:
    line=line.rstrip("\n")
    if os.path.exists(line):
        size=os.path.getsize(line)
        print(size,line,sep="<+>")
