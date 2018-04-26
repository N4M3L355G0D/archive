from pyzbar.pyzbar import *
import cv2,os,sys


def checkExists(file):
    if os.path.exists(file):
        if os.path.isfile(file):
            return file
        else:
            return [None,'notfile']
    else:
        return [None,'notexist']

def readbars(file):
    print(file,end=':')
    file=checkExists(file)
    if type(file) != list:
        img=cv2.imread(file)
        data=decode(img)
        if data != []:
            print(data)
        else:
            print("img did not contain a valid barcode")
    else:
        print(file[1])
        exit(1)

files=sorted([i for i in os.listdir('.') if os.path.splitext(i)[1] in ['.png','.jpg']])

for file in files:
    readbars(file)
