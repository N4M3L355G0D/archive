#! /usr/bin/env python2
import string
import base64
def checkNum(num=''):
    badchars=string.ascii_letters+string.punctuation+string.whitespace
    if num != '':
        if type(num) != type(str()):
            num=str(num)
        for char in num:
            if char in badchars:
                return 1
        return 0
    else:
        return 1

def main():
    MaxStr=''
    dumbMessage="apparently you do not know what a number is... why should I help you?"
    message="I will not throw paper airplanes in class"
    egg=b"WW91IGhhdmUgZGlzY292ZXJlZCBteSBlYXN0ZXIgZWdnISBEbyBiZSBhIGRpY2sgYWJvdXQgaXQhIEdGWSEK"
    dumbCounter=1
    countOut=20
    while checkNum(MaxStr) == 1:
        MaxStr=raw_input("How many lines do you want me to write for you? : ")
        if MaxStr == "#triggered":
            print str(base64.b64decode(egg)).rstrip("\n")
        if countOut <= dumbCounter:
            exit(dumbMessage)
        dumbCounter+=1

    for line in range(0,int(MaxStr)):
        print "{} : {}".format(line+1,message)

main()
