#! /usr/bin/python3

path="./final"
one=open(path+"/bigger","r")
two=open(path+"/smaller","r")

unique=list()

oneList=list()
twoList=list()

for i in one:
    oneList.append(i.rstrip("\n"))
for i in two:
    twoList.append(i.rstrip("\n"))
for i in oneList:
    if i not in twoList:
        if i not in unique:
            unique.append(i)

for i in unique:
    print(i)

