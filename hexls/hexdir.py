#! /usr/bin/python3

import os,sys, binascii

if len(sys.argv) >= 2:
 try:
  length=int(sys.argv[1])
  if length == 0:
   length=int(len(sys.argv[1]))
 except:
  length=int(len(sys.argv[1]))

 dir=os.urandom(length)
 hexdir=binascii.hexlify(dir)
 print(b"-0x-> "+hexdir+b" <-0x- =>"+dir)
 os.mkdir(dir)
else:
 print("please provide dir length integer or a string of desired dir length")
