#! /usr/bin/env python3
#NoGuiLinux
import matplotlib.pyplot as plt
import csv
import os
import re


os.chdir('C:\Data\Visualizing')
x=[]
y=[]

with open('test111.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[1])
        y.append(row[5])
        orig=y

    def sortAlistBySize2(orig):
    #this is my recommended method
        newlist=[]
        letters=[]
        finalList=[]
        counter=0
        #engineering notation
        l=['K','M','G','T','P','E']
        for i in orig:
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
                    finalList.append(orig[num])
        return finalList

    print(orig)
    orig=sortAlistBySize2(orig)
    print(orig)

