#! /usr/bin/python2

import os,sys,binascii,binhex

if sys.argv[1] != "--no-nf":
    with open(sys.argv[1],"rb") as f:
        for i in f:
            print("name file data: "+binascii.hexlify(i)+"\n------------------")

for num,x in enumerate(sys.argv):
    if num > 1:
        for i in os.listdir(x):
            #need to print hex
            try:
                test=i.encode()
                print(i)
            except:
                a=os.path.splitext(i)
                namehex=binascii.hexlify(a[0])
                if sys.argv[1] == "--no-nf":
                    namefile=open(namehex+".nf","wb")
                    namefile.write(binascii.unhexlify(namehex))
                    print("\nNF: "+namehex+".nf")
                else:
                    print("\nNF: "+sys.argv[1])
                print("-0x-> "+namehex+a[1]+" <-0x- => "+i+"\n")

