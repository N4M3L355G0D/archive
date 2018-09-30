#! /usr/bin/python3

hi=list()
lo=dict()
HI=0
LO=0
with open("text.tmp","r") as cfg:
    for i in cfg:
        spit=i.split("<+>")
        lo[spit[0]]=spit[1]
        #print(lo.values())

hi=sorted(lo.keys(),key=int)

for i in hi:
    print(lo[i].rstrip("\n"))
            
