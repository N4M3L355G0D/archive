#! /usr/bin/python3
def byteGen():
    byte="0123456789abfdef"
    
    for i in byte:
        for j in byte:
            yield ''.join((i,j))

a=list()
for i in range(0,12):
 a.append(byteGen())


for b in a[0]:
    for c in  a[1]:
        for d in a[2]:
            for e in a[3]:
                for f in a[4]:
                    for g in a[5]:
                        for h in a[6]:
                            for i in  a[7]:
                                for j in a[8]:
                                    for k in a[9]:
                                        for l in a[10]:
                                            for m in a[11]:
                                                print(b,c,d,e,f,g,h,i,j,k,l,m)
