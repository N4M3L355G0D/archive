#! /usr/bin/env python3
#NoGuiLinux
orig=['2.0G','1.1G','56M','5.0G','211G','4.8G','13G','7.2G']

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
