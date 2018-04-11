#! /usr/bin/env python3
#NoGuiLinux
import matplotlib.pyplot as plt
import csv
import os
import re

try:
    os.chdir('C:\Data\Visualizing')
except:
    pass
x=[]
y=[]
xy=[]
rows=[]
with open('test111.csv','r') as csvfile:
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
    modded_results=[]
    for row in results:
        size=row[0]
        ip=row[1]
        device=row[2]

        #xAxisLabel
        xAxis="{}({})".format(device,ip.replace(",","."))
        #yAxis
        yAxis=size
        #this is a list with the unique x axis see the xaxis variable
        modded_results.append([xAxis,yAxis])
    return modded_results

maxColor=4.0
#fake labels for x can be put in here, make sure it is as long as the data from the csv
custom=[]
#prefill the custom labels variable custom
#rows is a list containing the data rows/lines, so you need to get the length of that list using len(rows)
for i in range(0,len(rows)):
    custom.append(i)
#store the data in data
data=display()
#begin iteration run

for x,y in data:
    color='blue'
    #print(x,y)
    #print (x)
    #print (y[:-1])
    plt.xticks(rotation=90)
    #anything below a GB is obviously going to be less than 4GB
    if y[-1].upper() in ['K','M']:
        color='red'
    #now since we want anything below 4 in the G section to be red
    elif float(y[:-1]) < maxColor and y[-1].upper() == 'G':
        color='red'
    #now since in engineering notation, T/P/E are above G we really do not need to worry about it
    #the numbers are in y[:-1] which slices to to the end of the string minus one so '100T' becomes '100'
    #the engineering notation are in y[-1] which takes the last character of the string
    #so '100T' becomes 'T'
    #for colors to be changed, you need to use the color argument for plt.bar
    plt.bar(x,y,color=color,label='Loaded From File')

    
        


#plt.bar(x,y ,label='Loaded From File')


plt.xlabel = ('IP')
plt.ylabel=('Size')
plt.title('Visulizaing Data')
plt.show()

