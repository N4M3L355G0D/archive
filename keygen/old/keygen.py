#! /usr/bin/python3
import random, hashlib, platform, time

def keygen():
 ## get host data
 hostdata=''.join(platform.uname())
 ## convert time.localtime into string
 timenum=''
 for val in time.localtime():
  timenum=timenum+str(val)
 ## make a random nonce from timenum, which has been converted from an integer
 nonce2=str(random.randint(1,int(timenum)))
 
 ##combine the strings
 stringUnEncode=hostdata+timenum+nonce2
 ## binary encode the strings
 stringEncode=stringUnEncode.encode()
 
 #create the hash object
 pass1=hashlib.sha512()
 ## update the hash object with the string
 pass1.update(stringEncode)
 ## save the result
 result=pass1.hexdigest()
 
 
 ## break the result into a 8x16 space delimited string
 breaker=8
 
 password=[result[i:i+breaker] for i in range(0,len(result),breaker)]
 passAccum=''
 for i in password:
  passAccum=passAccum+i+" "
 
 ## print the result
 print(passAccum)
 return passAccum

keygen()
