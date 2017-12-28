#! /usr/bin/env python2
import os,shutil,sqlite3

import argparse

def main():
    #copy old faulty dir to new location, substituting bad chars with numeric equivalent
    location=str(raw_input("location: "))
    newtop='/tmp/'+str(raw_input("tmp dir: "))
    excl="\'\""

    for root,dirname,fnames in os.walk(location):
        rootAcc=''
        for char in root:
            if char in excl:
                rootAcc+="_"+str(ord(char))
            else:
                rootAcc+=char
        new=newtop+rootAcc
        if not os.path.exists(new):
            os.makedirs(new)
        print root,"|",new
    
    for root,dirname,fnames in os.walk(location):
        rootAcc=''
        for char in root:
            if char in excl:
                rootAcc+="_"+str(ord(char))
            else:
                rootAcc+=char
        new=newtop+rootAcc
        for fname in fnames:
            fnameAcc=''
            for char in fname:
                if char in excl:
                    fnameAcc+="_"+str(ord(char))
                else:
                    fnameAcc+=char
            newPath=os.path.join(new,fnameAcc)
            oldPath=os.path.join(root,fname)
            print oldPath+"|"+newPath
            if os.path.exists(oldPath):
                shutil.copy2(oldPath,newPath)
            else:
                print oldPath+"|"+newPath+"|Ignore as broken"
    print "fixed data structure located at : {}".format(newtop)
    #tarball the new structure at a later date

#create a function that makes a sha512sum of the src file and the dst file
#create a db where each row would consist of rowid,src filename,src sha512sum, dst filename, dst sha512sum
main()
