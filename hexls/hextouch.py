#! /usr/bin/python3

import os,sys,binascii

if len(sys.argv) >= 2:
    prefix=binascii.unhexlify(os.path.splitext(sys.argv[1])[0])
    ext=os.path.splitext(sys.argv[1])[1].encode()
    of=open(prefix+ext,"wb")
    of.write(b"")
    print(prefix+ext)
else:
    print("please provide a name that consists of hex-prefix and an ascii extension")

