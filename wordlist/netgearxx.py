#! /usr/bin/python3

import sys

adjective=open("adjectives.txt","r")
nouns=open("nouns.txt","r")
xxx=range(0,1000)

file="netgearxx.txt"
ofile=open(file,"w")

for i in adjective:
    for j in nouns:
        for k in xxx:
            final=i.rstrip("\n")+j.rstrip("\n")+str(k)
            if len(sys.argv) < 2:
             print(final)
            else:
             if sys.argv[1] == "--stdout":
                 print(final)
             elif sys.argv[1] == "--file":
                ofile.write(final+"\n")
             else:
                 print(final)
    #after each time the nouns file is complete it is closed, so reopen the file so wordlist does not stop after the first line of adjectives
    nouns=open("nouns.txt","r")
ofile.close()
