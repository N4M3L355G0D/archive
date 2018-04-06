#! /usr/bin/env python3

orig=['2.0G','1.1G','56M','5.0G','211G','4.8G','13G','7.2G']

def sortAlistBySize():
        
    origDict={str(index):{num[:len(num)-1]:num[-1].upper()} for index,num in enumerate(orig)}
    newlist=[]
    sortedList=[]
    
    for index in origDict.keys():
        for size in origDict[index]:
            engineering=origDict[index][size]
            size=float(size)
            if engineering == 'M':
                size=size*(1024**2)
            if engineering == 'G':
                size=size*(1024**3)
            newlist.append(size)
    newlist=sorted(newlist)
    for ele in newlist:
        if  1024**2 < ele < 1024**3:
            sortedList.append('{}{}'.format(ele/1024**2,'M'))
        elif 1024**3 < ele < 1024**4:
            sortedList.append('{}{}'.format(ele/1024**3,'G'))
    print(sortedList)

def sortAlistBySize2():
    newlist=[]
    letters=[]
    l=['K','M','G']
    for i in orig:
        if i[-1].upper() not in letters:
            letters.append(i[-1].upper())

    for size in l:
        if size in letters:
            newlist.extend([str(j)+size for j in sorted([float(i[:len(i)-1]) for i in orig if i[-1].upper() == size])])
    return newlist

a=sortAlistBySize2()
print(a)
