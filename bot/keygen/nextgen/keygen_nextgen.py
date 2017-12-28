#! /usr/bin/python3
#global
import time, random,hashlib,platform, os,sys, argparse



class keygen():
    def __init__(self):
        pass
    noDelim=False
    passString=str()
    def password(self):
        text=self.hashed(self.passString)
        return [text,self.passString]

    def hashed(self,string):
        passHash=hashlib.md5()
        passHash.update(string.encode())
        passFinal=passHash.hexdigest()
        passDigest=passHash.digest()
        return [passFinal,string,passDigest]

    def timeNum(self):
        tacc=str()
        for i in time.localtime():
            tacc=tacc+str(i)
        text=self.hashed(tacc)
        return [text,tacc]

    def timeList(self):
        tac=list()
        for i in time.localtime():
            rtac=random.randint(0,i)
            tac.append(str(rtac))
        text=self.hashed(''.join(tac))
        return [text,''.join(tac)]

    def pfData(self):
        pfDT=''.join(platform.uname())
        text=self.hashed(pfDT)
        return [text,pfDT]
    def nonceTotal(self):
        string=list()
        stringStr=str()
        for i in range(0,2):
            string.append(self.timeList()[i])
            string.append(self.timeNum()[i])
            string.append(self.pfData()[i])
            string.append(self.password()[i])
        for i in string:
            stringStr+=str(i)
        text=self.hashed(stringStr)
        if self.noDelim == False:
            key=self.breakIt(text[0])
        else:
            key=text[2]
        return key
    
    def breakIt(self,string):
        delim="-"
        breaker=8
        passAcc=""
        text=[string[i:i+breaker] for i in range(0,len(string),breaker)]
        for count,chunk in enumerate(text):
            if count < 3:
                passAcc=passAcc+chunk+delim
            else:
                passAcc=passAcc+chunk
        return passAcc

#a=keygen()
#a.passString="one"
#b=a.nonceTotal()
#print(b)
