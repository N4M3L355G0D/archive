#! /usr/bin/python3

import psutil,math, time

memdata=psutil.virtual_memory()

print(memdata.percent)
acc=str()

accL=list()

for i in range(0,int(math.pow(4096,2))):
 accL.append(" ")

print(type(memdata.percent))

x=1
while x == 1:
 memdata=psutil.virtual_memory()
 if float(memdata.percent) < float(80.0):
  acc+=''.join(accL)
 else:
  time.sleep(90)
 print(memdata.percent)
