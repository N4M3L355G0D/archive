#! /usr/bin/env python3
#NoGuiLinux
import matplotlib.pyplot as plt
import csv
import os
import re


#os.chdir('C:\Data\Visualizing')
x=[]
y=[]
xy=[]
with open('test1111.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[5])
        y.append(row[1])
        xy.append([row[5],row[1],row[2]])
        orig=x

def sortAlistBySize2(origin):
    #this is my recommended method
    newlist=[]
    letters=[]
    finalList=[]
    counter=0
    #engineering notation
    l=['K','M','G','T','P','E']
    for i in origin:
        if i[-1].upper() not in letters:
            letters.append(i[-1].upper())
    #set the newlist according to float values grouped by engineering values
    for size in l:
        if size in letters:
            newlist.extend([str(j)+size for j in sorted([float(i[:len(i)-1]) for i in orig if i[-1].upper() == size])])
    #now lets retrieve the equivalent values from the original list so that we keep the original values that were input
    for size in newlist:
        for num,ele in enumerate(orig):
            ele=str(float(ele[:-1]))+ele[-1]
            if ele == size:
                finalList.append(origin[num])
    return finalList

def alignIp2Size(unsortedSizes,ipsAndSizes):
    final=[]
    sortedSizes=sortAlistBySize2(unsortedSizes)
    sortedLen=len(ipsAndSizes)
    for size in sortedSizes: 
        for row in ipsAndSizes:
            if size in row:
                if row not in final:
                    final.append(row)
    return final

def display():
    results=alignIp2Size(orig,xy)
    for row in results:
        size=row[0]
        ip=row[1]
        device=row[2]
        print(device,size,ip.replace(",","."))
display()
