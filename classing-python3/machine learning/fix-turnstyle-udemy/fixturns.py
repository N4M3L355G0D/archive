#! /usr/bin/env python3

import csv,pandas


filenames=["turnstile_110507.txt"]
chunk=5
udKeyword="updated_"
for file in filenames:
    with open(file,'r') as idata, open(udKeyword+file,"wb") as odata:
        data=csv.reader(idata,delimiter=",")
        for row in data:
            rowId=row[:3]
            rowE=row[3:]
            d=[rowE[i:i+chunk] for i in range(0,len(rowE),chunk)]
            for i in d:
                for num,l in enumerate(i):
                    i[num]=i[num].strip(' ')
                rowA=[]
                rowA.extend(rowId)
                rowA.extend(i)
                entry=','.join(rowA)+"\n"
                odata.write(entry.encode())
