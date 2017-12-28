#! /usr/bin/python3

import random,keygen_nextgen

from Crypto.Cipher import AES

class eCrypt():
    keyfile="keyfile.bin"
    message="message.aes"
    demo=True
    ofile=True
    def __init__(self):
        pass
    def init(self):
        if self.demo == True:
            self.dem()
            self.encrypt()

    def stringFix(self,text):
        while len(text) < 32 != 0:
            text+=text
        return int(text)

    def printKey(self):
        print("key: ",self.key)

    key=str()
    printVal={'encrypt':False,'dem':False,'decrypt':False}
    text=str()
    def dem(self):
        if self.demo == True:
            startStr=self.stringFix('1')
            endStr=self.stringFix('9')
            self.key=str(random.randint(startStr,endStr))
            self.printKey()

    def pad(self,text,key):
        keylen=len(key)
        while len(text) % keylen != 0:
            text+= ' '
        return text
    def encrypt(self):
        aes=AES.new(self.key)
        padded_text=self.pad(self.text,self.key)
        encrypted_text=aes.encrypt(padded_text)
        if self.demo == True or self.printVal['encrypt'] == True :
            if self.demo == False:
                self.printKey()
            print("text: ",self.text)
            print("encrypted text: ",encrypted_text)
            #will be change to variable file name
        if self.ofile == True:
            file=open(self.message,"wb")
            file.write(encrypted_text)
            file.close()
    def iterate(self,data):
        acc=bytes()
        for i in data:
            acc+=i
        return acc

    def decrypt(self):
        kacc=bytes()
        macc=bytes()
        key=open(self.keyfile,"rb")
        message=open(self.message,"rb")
        
        kacc=self.iterate(key)
        macc=self.iterate(message)

        a=AES.AESCipher(kacc)
        dmesg=a.decrypt(macc)
        if self.printVal['decrypt'] == True:
            print(dmesg)
        return dmesg

"""
Key=keygen_nextgen.keygen()
Key.noDelim=True

d=eCrypt()
d.demo=False
d.printVal['encrypt']=False
d.printVal['decrypt']=True
d.key=Key.nonceTotal()
file=open(d.keyfile,"wb")
file.write(d.key)
file.close()

d.text="wow"
'''use a default keygen(), rather weak, but will do in a pinch'''
#d.init()
d.encrypt()
d.decrypt()"""
