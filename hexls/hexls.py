#! /usr/bin/python2

import os,sys,binascii,binhex,argparse

parser=argparse.ArgumentParser()
parser.add_argument("-n","--name-file")
parser.add_argument("-d","--path")
parser.add_argument("-H","--hex-only",action="store_true")
options=parser.parse_args()

if len(sys.argv) < 2:
    print("you must provide, two arguments")
    exit()

if options.name_file != "no-nf":
 if os.path.exists(options.name_file):
  with open(options.name_file,"rb") as f:
   for i in f:
    print("name file data: "+binascii.hexlify(i).decode()+"\n------------------")
 else:
  print("ERROR: non-existant name file - "+options.name_file)
  exit()


for i in os.listdir(options.path.encode()):
 try:
  assert(i.decode())
  if options.hex_only != True:
   print(i.decode())
 except:
  a=os.path.splitext(i)
  namehex=binascii.hexlify(a[0])
  if options.name_file == "no-nf":
   namefile=open(namehex+b".nf","wb")
   namefile.write(binascii.unhexlify(namehex))
   print(b"\nNF: "+namehex+b".nf")
  else:
   print("\nNF: "+sys.argv[1])
  print(b"-0x-> "+namehex+a[1]+b" <-0x- => "+i)

