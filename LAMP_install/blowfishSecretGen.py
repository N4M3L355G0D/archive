#! /usr/bin/python3
import hashlib, time, random,sys

## generate the 32 char blowfish secret for phpMyAdmin

timeAcc=''
for i in time.localtime():
 timeAcc=timeAcc+str(i)

if len(sys.argv) > 1:
 secret=sys.argv[1]
else:
 secret=input("Enter a Secret, then press enter: ")


data_string=str(secret)+str(random.random())+str(time.ctime())+str(random.randint(0,int(timeAcc)))

hobject=hashlib.sha512()
hobject.update(data_string.encode())
result=hobject.hexdigest()
## print 32 chars of secret
resultAcc=""
for i,j in enumerate(result):
 if i < 32:
  resultAcc=resultAcc+j
 else:
  break
print(resultAcc)
