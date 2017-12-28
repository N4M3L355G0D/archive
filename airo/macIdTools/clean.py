#! /usr/bin/python3
import sys
#create 
finalPath="./final"
tmpPath="./tmp"

try:
 one=open(tmpPath+"/smaller.tmp","r")
 two=open(tmpPath+"/bigger.tmp","r")
except OSError as error:
    print(error)
    #the script should end here, but on the off chance that it does not
    sys.exit()
    

twolist=list()
onelist=list()

unique_one=list()
unique_two=list()

for i in one:
    onelist.append(i)

for i in two:
    twolist.append(i)

one.close()
two.close()

for i in twolist:
    if i not in unique_two:
        unique_two.append(i)
for i in onelist:
    if i not in unique_one:
        unique_one.append(i)
one=open(finalPath+"/smaller","w")
two=open(finalPath+"/bigger","w")

for i in unique_one:
    print(i.rstrip("\n"),"#1")
    one.write(i)
for i in unique_two:
    print(i.rstrip("\n"),"#2")
    two.write(i)
one.close()
two.close()
