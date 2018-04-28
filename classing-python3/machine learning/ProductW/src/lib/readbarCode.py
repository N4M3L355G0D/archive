#! /usr/bin/env python3
#NoGuiLinux
from pyzbar.pyzbar import *
from pyzbar.pyzbar import ZBarSymbol
import cv2,os,sys

class readBars:
    master=None

    def checkExists(self,file):
        if os.path.exists(file):
            if os.path.isfile(file):
                return file
            else:
                return [None,'notfile']
        else:
            return [None,'notexist']

    def readbars(self,file,mem=None):
        print(file,end=':')
        if mem == None:
            file=self.checkExists(file)
        if type(file) != list or (mem != None):
            if mem == None:
                img=cv2.imread(file)
            else:
                img=file
            try:
                data=decode(img)
            except OSError as e:
                print(e)
                data=[]

            if data != []:
                print(data)
                return data
            else:
                print("img did not contain a valid barcode")
                return False
        else:
            print(file[1])
            return False

if __name__ == "__main__":
    rEddit=readBars()
    files=sorted([i for i in os.listdir('.') if os.path.splitext(i)[1] in ['.png','.jpg']])
    for file in files:
        rEddit.readbars(file)
