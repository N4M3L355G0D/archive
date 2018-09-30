#! /usr/bin/env python2
import base64
import sys
import os

if len(sys.argv) == 3:
 mode=sys.argv[1]
 infile=sys.argv[2]
 if mode == "encode":
  if os.path.exists(infile):
   ofile=sys.argv[2]+".b64"
   okay=open(ofile,"wb")
   with open(sys.argv[2],"rb") as indata:
    sect=''
    while True:
     chunk = indata.read(1024)
     if chunk == '':
      break
     sect+=chunk
    odata=base64.b64encode(sect)
    okay.write(odata)
  else:
   print "does not exist: {}".format(infile)
 if mode == "decode":
  infile=sys.argv[2]
  if os.path.exists(infile):
   ofile=infile.replace(".b64","")
   okay=open(ofile,"wb")
   with open(infile,"rb") as indata:
    sect=''
    while True:
     chunk = indata.read(1024)
     if chunk == '':
      break
     sect+=chunk
    odata=base64.b64decode(sect)
    okay.write(odata)
  else:
   print "does not exist: {}".format(infile)
else:
 print "two arguments are required! mode [encode||decode] fname []"
