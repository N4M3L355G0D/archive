#! /usr/bin/env python3
#you need to do
#look up slurping and sipping in python
#using the methods here, you will be sipping, so you can handle large files that are larger than your system memory
chunkSize=128
#rb is read binary which less prone to issues with files that contain non-Ascii
#r just reads the file strings, and can exit if non-ascii data is found in the file, and will add a \n to the line end
#rb is my prefered method
#sometimes using 'c' like language helps some, and i know 'c' so, win-win
mode='rb'
fpath='D:\days.txt'
def oneWay():
    with open(fpath,mode) as data: 
        while True: 
            #read the file iostream in chunkSize
            d=data.read(chunkSize) 
            #if d is an eof, then break from the loop, and close the iostream data
            if not data: 
                break
            #print the data obtained from the iostream
            print(d)

def anotherWay():
    data=open(fpath,mode)
    while True:
        d=data.read(chunkSize)
        if not d:
            break
        print(d)
    data.close()

