#! /usr/bin/python3
import math
print((7*26)+17)

const=1
lineNumber=200-const
count=list()
for i in range(0,4):
    if lineNumber > math.pow(26,i):
        count.append(i)
    else:
        break
print("in the character space of 4, from left to right, everything that is before",count,"character space, will be 'a'")


##need a recursive version of below
for i in range(1,27):
    for j in range(1,27):
        if ((i*26)+j) == lineNumber:
            print(i,j)
